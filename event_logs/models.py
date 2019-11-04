from django.db import models

class Event_Logs(models.Model):
	id = models.AutoField(primary_key=True)
	event_date = models.TextField()
	title = models.TextField()
	location = models.TextField()
	host = models.TextField()
	start = models.CharField(max_length=8)
	end = models.CharField(max_length=8)
	
# Create your models here.
