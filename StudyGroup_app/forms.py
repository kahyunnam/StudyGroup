from django import forms

from .models import Course, Message

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['Course_Name']
		labels = {'Course_Name':''}

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['message_text']
		labels = {'message_text':'Message:'}
		widgets = {'message_text':forms.Textarea}