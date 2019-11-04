from django.db import models
from program.models import Program

class Student(models.Model):
	id = models.AutoField(primary_key=True)
	gender = models.TextField()
	first_name = models.TextField()
	middle_initial = models.TextField()
	last_name = models.TextField()

	GRADE_LEVELS = [
		('FR','FRESHMAN'),
		('SP','SOPHOMORE'),
		('JR','JUNIOR'),
		('SR','SENIOR'),
	]

	level = models.CharField(max_length=2, choices=GRADE_LEVELS)
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	street = models.TextField()
	city = models. TextField()
	us_state = models.CharField(max_length=2)
	zip_code = models.IntegerField()
	email = models.EmailField(null=True)
	password = models.TextField(null=True)
	phone = models.CharField(max_length=14)
	country_code = models.IntegerField(default=1)
	birthdate = models.DateField()
	ssan = models.CharField(max_length=11)
	weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	height = models.CharField(max_length=6, null=True)

# Create your models here.
