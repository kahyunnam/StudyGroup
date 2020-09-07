from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .models import Course, Message
from .forms import CourseForm, MessageForm

def home(request):
	"""The home page for Study Group"""
	courses = Course.objects.order_by('Course_Name')
	context = {'courses':courses}
	return render(request, 'StudyGroup_app/home.html',context)

def coursemessage(request, course_id):
	"""show message room for specific course"""
	course = Course.objects.get(id = course_id)
	messages = course.message_set.order_by('-date_added', '-time_added')
	context = {'course':course, 'messages':messages}
	return render(request, 'StudyGroup_app/coursemessage.html', context)

def course_form(request):
	
	"""Add a new course"""
	if request.method !='POST':
		form = CourseForm()
		courses = Course.objects.order_by('Course_Name')
		context = {'courses':courses}
	else:
		
		form = CourseForm(data=request.POST)
		if form.is_valid():
			new_course = form.save(commit = False)
			new_course.owner = request.user
			new_course.save()
			return redirect('StudyGroup_app:home')

	context = {'form':form}
	return render(request, 'StudyGroup_app/new_course.html',context)

def new_message(request, course_id):
	course = Course.objects.get(id = course_id)

	if request.method != 'POST':
		form = MessageForm()

	else:
		form = MessageForm(data=request.POST)
		if form.is_valid():
			new_message = form.save(commit=False)
			new_message.course = course

			new_message.owner = request.user

			new_message.save()

			return redirect('StudyGroup_app:coursemessage', course_id = course_id)

	context = {'course':course, 'form':form}
	return render(request, 'StudyGroup_app/new_message.html',context)	


