from django.db import models

class Task(models.Model):
    id_task=models.CharField(max_length=64)
    n_task=models.CharField(max_length=64)
    dc_task=models.CharField(max_length=64)
    dr_task=models.CharField(max_length=64)
    

  

# Create your models here.
