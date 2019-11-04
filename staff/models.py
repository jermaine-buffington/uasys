from django.db import models
from department.models import Department

# Create your models here.
class Staff(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.TextField()
	middle_initial = models.CharField(max_length=1)
	last_name = models.TextField()

	GENDER_CHOICES = [
		('M', 'Male'),
		('F', 'Female'),
		]

	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	STAFF_ROLES = [
		('PS', 'President'),
		('PR', 'Provost'),
		('DH', 'Dean / Department Head'),
		('AD', 'Assistant Dean'),
		('TB', 'Trustee Board Member'),
		('AF', 'Adjunct Faculty Member'),
		('TF', 'Tenured Faculty Member'),
		('TA', 'Teacher Assistant'),
		('AM', 'Administrator'),
		]

	role = models.CharField(max_length=2, choices=STAFF_ROLES)

	department = models.ForeignKey(Department, on_delete=models.CASCADE)

	street_address = models.TextField()
	city = models.TextField()
	us_state = models.TextField("state")
	zip_code = models.TextField()
	email = models.TextField()
	password = models.TextField()
	phone = models.CharField(max_length=12)
	country_code = models.IntegerField()
	birth_date = models.DateField()
	ssan = models.CharField(max_length=12)
