from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from file.models import Employee_Task
from .customPermission import MyPermission
from .serializers import EmployeetaskSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    print("-----------------------------------shayad run kiya hai")
    print(request.user.username)
    api_urls={
        'token ':'/account/api/token',
        'token Refresh': '/account/api/token/refresh',
        'File upload':'/api/v1/file/create',
        'File Edit':'api/v1/file/update',
        'File Delete':'api/v1/file/delete',
        'View all Files':'api/v1/dashboard',
    }
    return Response({"code":200,"message":"API List to be implemented","data":api_urls},status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_all(request):
    data=EmployeetaskSerializer(Employee_Task.objects.all(),many=True).data
    return Response({"code":200,"message":"Fetched all the items","data":data},status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_details(request):
    try:
        id=request.data["emp_id"]
        data=EmployeetaskSerializer(Employee_Task.objects.get(emp_id=id)).data
        return Response({"code":200,"message":"Details of the item","data":data},status.HTTP_200_OK)
    except:
        return Response({"code":404,"message":"Not Found","data":[]},status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def FileUploadView(request):
    parser_class = (FileUploadParser,)    
    file_serializer = EmployeetaskSerializer(data=request.data)
    if file_serializer.is_valid():
          file_serializer.save()
          return Response({"code":201,"message":"Successfully Created the record","data":file_serializer.data}, status=status.HTTP_201_CREATED)
    else:
          return Response({"code":400,"message":"Something Error happened","data":file_serializer.error}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([MyPermission,IsAuthenticated])
def task_update(request):
    request_body = request.data
    obj = Employee_Task.objects.get(emp_id=request_body["emp_id"])
    if(request.user.username==obj.owner):
        obj.department = request_body["department"]
        obj.task = request_body["task"]
        obj.duedate = request_body["duedate"]
        obj.file = request_body["file"]
        obj.description =  request_body["file"]
        obj.save()
        return Response({"code":200,"message":"Successfully Updated the item","data":[]}, status.HTTP_200_OK)
    return Response({"code":403,"message":"Forbidden Not Allowed !","data":[]},status.HTTP_403_FORBIDDEN)

@api_view(["POST"])
@permission_classes([MyPermission])
def task_delete(request):
    try:
        request_body = request.data["emp_id"]
        obj = Employee_Task.objects.get(emp_id=request_body)
        print(request.user.username)
        if request.user.username==obj.owner:
            obj.delete()
            return Response({"code":200,"message":"Successfully deleted the item","data":[]},status.HTTP_200_OK)
        return Response({"code":403,"message":"Forbidden Not Allowed !","data":[]},status.HTTP_403_FORBIDDEN) 
    except:
        return Response({"code":401,"message":"Unauthorized or Not Found","data":[]},status.HTTP_404_NOT_FOUND)