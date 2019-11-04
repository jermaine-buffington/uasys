from django import forms

from .models import Action_Items
from staff.models import Staff

ADMIN_CHOICES = []

for admin in Staff.objects.filter(role='AM'):
		ADMIN_CHOICES.append((admin.id, admin.first_name + ' ' + admin.last_name))


class Action_Items_Form(forms.ModelForm):
	admins=forms.ChoiceField(choices=ADMIN_CHOICES, required=True)
	status=forms.ChoiceField(choices=Action_Items.ACTION_STATUS, required=False)
	
	class Meta:
		model = Action_Items
		fields = ['staff', 'assigned', 'desc', 'exp_date']