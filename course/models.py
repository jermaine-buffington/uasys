from django.db import models

# Create your models here.
class Course(models.Model):
	id = models.AutoField(primary_key=True)
	code = models.CharField(max_length=10)
	desc = models.CharField(max_length=150)
	credits = models.DecimalField(max_digits=1, decimal_places=2)

	COURSE_TYPES = [
		('GENED', 'GENERAL EDUCATION'),
		('COREC', 'CORE COURSES'),
		('CONCC', 'CONCENTRATION'),
		('ELECC', 'ELECTIVE'),
		('PREPP', 'PREPATORY'),
		('SPECC', 'SPECIALIZATION'),
	]

	course_type = models.CharField(max_length=5, choices=COURSE_TYPES)