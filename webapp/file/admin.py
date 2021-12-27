from django.contrib import admin
from .models import Employee_Task

# Register your models here.
@admin.register(Employee_Task)
class Assignment(admin.ModelAdmin):
    list_display=(
        "id","owner","emp_id","department","task","duedate","file","description"
    )