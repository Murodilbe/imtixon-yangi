from django.contrib import admin
from .models import  Lesson,  Student, Teacher, User, Comment
# Register your models here.
admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Comment)
