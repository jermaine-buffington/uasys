from django.db import models
from department.models import Department

class Program(models.Model):
	id = models.AutoField(primary_key=True)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)

# Create your models here.
