from django.db import models

class Task(models.Model):
    id_task=models.CharField(max_length=364)
    n_task=models.CharField(max_length=64)
    dc_task=models.CharField(max_length=364)
    dr_task=models.CharField(max_length=64)
    

  
class Employee(models.Model):
    id_employee=models.CharField(max_length=64)
    n_employee=models.CharField(max_length=64)
    task=models.ManyToManyField(Task,blank=True,related_name='employee')
# Create your models here.
    def __str__(self) :
        return f'{self.id_employee}, {self.n_employee}'