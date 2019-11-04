from django.db import models

from staff.models import Staff

class Action_Items(models.Model):
	id = models.AutoField(primary_key=True)
	staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
	assigned = models.TextField()
	desc = models.TextField()
	exp_date = models.TextField()

	ACTION_STATUS = [
		('NEW','NEW'),
		('IN PROGRESS','IN PROGRESS'),
		('COMP','COMPLETE'),
	]

	task_status = models.CharField(max_length=11, choices=ACTION_STATUS, default='NEW')

# Create your models here.
