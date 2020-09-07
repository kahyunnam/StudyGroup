from django.contrib import admin

# Register your models here.
from .models import Course, Message

admin.site.register(Course)
admin.site.register(Message)