import graphene
from graphene_django import DjangoObjectType
from .models import Employee_Task

class DepartmentType(DjangoObjectType):
    class Meta: 
        model = Employee_Task
        fields = ('id','department')

  
class TaskType(DjangoObjectType):
    class Meta: 
        model = Employee_Task
        fields = (
            'id',
            'owner',
            'emp_id',
            'department',
            'task',
            'duedate',
            'file',
            'description',
        )  


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)
    task_by_idx = graphene.Field(TaskType, idx=graphene.Int())
    tasks_by_department=graphene.List(TaskType,dep=graphene.String())

    def resolve_tasks(root, info, **kwargs):
        # Querying a list
        return Employee_Task.objects.all()
    
    def resolve_task_by_idx(root, info, idx):
        # Querying a single question
        return Employee_Task.objects.get(emp_id=idx)
    
    def resolve_tasks_by_name(root, info, name):
        # Querying a single question
        return Employee_Task.objects.get(owner=name)
    
    def resolve_tasks_by_department(root, info, dep):
        # Querying a single question
        return Employee_Task.objects.filter(department=dep)
    
schema = graphene.Schema(query=Query)