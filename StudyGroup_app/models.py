from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	"""forum page for specific course"""
	Course_Name = models.CharField(max_length = 9)
	#(Course_Name should be in formate of: "PHYS 1116",
	#   therefore shouldn't be longer than 9 characters)
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		"""return string representation of model"""
		return self.Course_Name


class Message(models.Model):
	"""message sent by student in course forum"""
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	message_text = models.TextField()
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateField(auto_now=True)
	time_added = models.TimeField(auto_now=True)
	

	class Meta:
		verbose_name_plural = 'messages'

	def __str__(self):
		"""Return a string representation of model"""
		return f"{self.message_text}"
