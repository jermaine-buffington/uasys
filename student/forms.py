from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from program.models import Program
GENDERS = [('M', 'Male'),('F','Female')]

GRADE_LEVELS = [
		('FR','FRESHMAN'),
		('SP','SOPHOMORE'),
		('JR','JUNIOR'),
		('SR','SENIOR'),
	]

PROG = []
for x in Program.objects.all():
	temp=(x.id, x.title)
	PROG.append(temp)



class EnrollmentForm(forms.Form):
	
	first_name = forms.CharField(label='First Name:', widget=forms.TextInput(attrs={'placeholder':'Student First Name'}))
	middle_initial = forms.CharField(label='M.I.:', max_length=1, widget=forms.TextInput())
	last_name = forms.CharField(label='Last Name:', widget=forms.TextInput(attrs={'placeholder':'Student Last Name'}))
	gender = forms.ChoiceField(label='Gender:', choices=GENDERS)
	street = forms.CharField(label='Street:', widget=forms.TextInput(attrs={'placeholder':'Student Address'}))
	city = forms.CharField(label='City:', widget=forms.TextInput)
	us_state = forms.CharField(label='State:', max_length=2)
	zip_code = forms.IntegerField(label='Zip Code:')
	level = forms.ChoiceField(label='Student Classification:', choices=GRADE_LEVELS)
	program = forms.ChoiceField(label='Major Course of Study:', choices=PROG)
	phone = forms.IntegerField(label='Phone:')
	birthdate = forms.DateField(label='Date of Birth:')
	ssan = forms.IntegerField(label='SSAN:')
	# weight = forms.IntegerField(label='Weight:', max_digits=5, decimal_places=2)
	# height = forms.CharField(label='Height:', max_length=6)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Row(
				Column('first_name', css_class='form-group col-md-4 mb-0'),
				Column('middle_initial', css_class='form-group col-md-1 mb-0'),
				Column('last_name', css_class='form-group col-md-4 mb-0'),
				Column('gender', css_class='form-group col-md-2 mb-0'),
				css_class='form-row' 
				),
			Row(
				Column('street', css_class='form-group col-md-4 mb-0'),
				Column('city', css_class='form-group col-md-4 mb-0'),
				Column('us_state', css_class='form-group col-md-1 mb-0'),
				Column('zip_code', css_class='form-group col-md-2 mb-0'),
				css_class='form-row'
				),
			Row(
				Column('phone', css_class='form-group col-md-4 mb-0'),
				Column('birthdate', css_class='form-group col-md-4 mb-0'),
				Column('ssan', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
				),
			Row(
				Column('level', css_class='form-group col-md-4 mb-0'),
				Column('program', css_class='form-group col-md-7 mb-0'),
				css_class='form-row'
				),

			Submit('submit', 'Save')

			)
