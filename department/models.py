from django.db import models

class Department(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)

# Create your models here.
