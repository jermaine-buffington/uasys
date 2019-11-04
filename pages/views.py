from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Max
from staff.models import Staff
from department.models import Department
from event_logs.models import Event_Logs
from event_logs.forms import Event_Log_Forms
from datetime import date
from action_items.models import Action_Items
from action_items.forms import Action_Items_Form
from student.models import Student
from student.forms import EnrollmentForm
from program.models import Program

# Create your views here.

def login_view (request, *args, **kwargs):
	return render(request, "login.html", {})

def profile_view(request, *args, **kwargs):
	admin_emp=Staff.objects.filter(role='AM')
	
	for emp in admin_emp:
		if emp.email == request.user.username:
			dept=Department.objects.get(id=emp.department_id)
			return render(request, "profile.html", {'emp':emp, 'dept':dept})

def home_view (request, *args, **kwargs):
	form=Event_Log_Forms()
	# Test if Request Method is "POST"
	if request.method == "POST":
		ev_date=request.POST.get(str('event_date'))
		ev_title=request.POST.get('title')
		ev_loc=request.POST.get('location')
		ev_host=request.POST.get('host')
		ev_start=request.POST.get('start')

		Event_Logs.objects.create(event_date=ev_date, title=ev_title, location=ev_loc,
			host=ev_host, start=ev_start)
		# Ensure form is valid
		# if form.is_valid:
		# 	# Create new Event_Logs object
		# 	Event_Logs.objects.create(**form.cleaned_data)

	# Load or Reload Page w/ New Event_Log Objects

	admin_emp=Staff.objects.filter(role='AM')
	events=Event_Logs.objects.all
	for emp in admin_emp:
		if emp.email == request.user.username:
			act_key=emp.id
			opt_action_status=Action_Items.ACTION_STATUS
			actions=Action_Items.objects.filter(staff_id=act_key)
			return render(request, "home.html", {'emp':emp, 'events':events, 'actions':actions, 
				'status':opt_action_status, 'new_event_form':form})

def new_event_view (request, *args, **kwargs):

	form=Event_Log_Forms()
	print("Accessed Through GET Method!!!")
	# Test if Request Method is "POST"
	if request.method == "POST":
		form=Event_Log_Forms(request.POST)
		print("Accessed Through POST Method!!!")
		print(request.POST.get('event_date'))
		print(request.POST.get('title'))
		print(request.POST.get('location'))
		print(request.POST.get('host'))
		print(request.POST.get('start'))
		# Ensure form is valid
		if form.is_valid:
			# Create new Event_Logs object
			Event_Logs.objects.create(**form.cleaned_data)

	# Load or Reload Page w/ New Event_Log Objects

	admin_emp=Staff.objects.filter(role='AM')
	events=Event_Logs.objects.all
	for emp in admin_emp:
		if emp.email == request.user.username:
			act_key=emp.id
			opt_action_status=Action_Items.ACTION_STATUS
			actions=Action_Items.objects.filter(staff_id=act_key)
			return render(request, "home.html", {'emp':emp, 'events':events, 'actions':actions, 
				'status':opt_action_status, 'new_event_form':form})

def new_action_view (request, *args, **kwargs):

	form=Action_Items_Form()
	# Test if Request Method is "POST"
	if request.method == "POST":

		act_staff=request.POST.get('staff')
		act_assigned=request.POST.get(str('assigned'))
		act_desc=request.POST.get('desc')
		act_exp_date=request.POST.get(str('exp_date'))

		Action_Items.objects.create(staff=act_staff, assigned=act_assigned, desc=act_desc,
			exp_date=act_exp_date, task_status='NEW', id=Action_Items.objects.all().aggregate(Max('id'))['id__max'])
		# Ensure form is valid
		# if form.is_valid:
		# 	# Create new Event_Logs object
		# 	Event_Logs.objects.create(**form.cleaned_data)

	# Load or Reload Page w/ New Event_Log Objects

	admin_emp=Staff.objects.filter(role='AM')
	events=Event_Logs.objects.all
	for emp in admin_emp:
		if emp.email == request.user.username:
			act_key=emp.id
			opt_action_status=Action_Items.ACTION_STATUS
			actions=Action_Items.objects.filter(staff_id=act_key)
			return render(request, "home.html", {'emp':emp, 'events':events, 'actions':actions, 
				'status':opt_action_status, 'new_action_form':form})

def enrollment_view(request, *args, **kwargs):
	form=EnrollmentForm()

	if request.method == 'POST':
		en_gender=request.POST.get('gender')
		en_first=request.POST.get('first_name')
		en_middle=request.POST.get('middle_initial')
		en_last=request.POST.get('last_name')
		en_level=request.POST.get('level')
		en_prog=Program.objects.get(id=request.POST.get('program'))
		en_street=request.POST.get('street')
		en_city=request.POST.get('city')
		en_us_state=request.POST.get('us_state')
		en_zip=request.POST.get('zip_code')
		en_email=request.POST.get('email')
		en_pswd='ch@ng3m3n0w'
		en_phone=request.POST.get('phone')
		en_dob=request.POST.get('birthdate')
		en_ssan=request.POST.get('ssan')

		Student.objects.create(gender=en_gender, first_name=en_first, middle_initial=en_middle, last_name=en_last, level=en_level,
			program=en_prog, street=en_street, city=en_city, us_state=en_us_state, zip_code=en_zip, email=en_email, password=en_pswd,
			phone=en_phone, birthdate=en_dob, ssan=en_ssan)

	admin_emp=Staff.objects.filter(role='AM')
	for emp in admin_emp:
		if emp.email == request.user.username:
			return render(request, "enroll.html", {'form':form, 'emp':emp})


