from django.urls import path
from . import views

urlpatterns=[
        path('',views.apiOverview,name="api-overview"),
        path('task_all',views.task_all,name='getall'),
        path('task_details',views.task_details,name='task_details'),
        path('task_upload',views.FileUploadView,name="upload"),
        path('task_update',views.task_update,name="task_update"),
        path('task_delete',views.task_delete,name='task_delete'),
        path('submitted',views.submitted,name='submitted_stats'),
]