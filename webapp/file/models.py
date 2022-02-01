from django.db import models
from django_minio_backend import MinioBackend, iso_date_prefix, __name__;

from webapp.settings import MINIO_MEDIA_FILES_BUCKET

# Create your models here.
class Employee_Task(models.Model):
    
    def nameFile(instance,filename):
        return '/'.join(['data',str(instance.owner),filename])
    
    #id=models.AutoField("ID")
    emp_id=models.CharField("Emp_ID",max_length=18)
    owner=models.CharField("Owner",max_length=20)
    department=models.CharField("Department",max_length=25)
    task=models.CharField("task",max_length=25)
    duedate=models.DateField("Due Date (mm/dd/yy)",auto_now_add=False,auto_now=False)
    file = models.FileField(verbose_name="File",
                            storage=MinioBackend(bucket_name=MINIO_MEDIA_FILES_BUCKET),
                            upload_to=nameFile)
    description=models.TextField("Description",max_length=100)

    def __str__(self):
        return self.file.name

    class Meta:
        db_table='employee_task'
    