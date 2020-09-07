"""Defines url patterns for StudyGroup_app"""

from django.urls import path

from . import views

app_name = 'StudyGroup_app'
urlpatterns = [
	# Home page
	path('', views.home, name = 'home'),
	# Message board for individual course
	path('<int:course_id>/', views.coursemessage, name = 'coursemessage'),
	# page for adding a new course
	path('new_course/', views.course_form, name = 'new_course'),
	# page for adding a new entry
	path('new_message/<int:course_id>/', views.new_message, name = 'new_message'),
]