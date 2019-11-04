from django import forms
from .models import Event_Logs

class Event_Log_Forms(forms.ModelForm):
	class Meta:
		model = Event_Logs
		fields = ['event_date', 'title', 'location', 'host', 'start']