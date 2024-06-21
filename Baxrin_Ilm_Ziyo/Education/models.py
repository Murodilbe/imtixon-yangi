from django.contrib.auth.models import User,Group,Permission
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Dars nomi')
    created = models.DateTimeField(verbose_name='Dars boshlangan sana')
    price = models.CharField(max_length=150,verbose_name='Darsning bir oylik haqqi')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    video = models.FileField(upload_to='education/', verbose_name='dars videosi',null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov'])],
                             help_text='Video yuklang')
    score = models.IntegerField(verbose_name='Darsga qo\'yilgan baxo' ,null=True,validators=[validators.MaxValueValidator(100,'Chegaralangan miqdor'), validators.MinValueValidator(0,'Minimal miqdor')],
                                help_text='Darsni Baholang')




    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(verbose_name='Dars o\'tuvchi o\'qituvchi', max_length=150)
    age = models.DateField(verbose_name='O\'qituvchini yoshi', max_length=150)
    status = models.IntegerField(verbose_name='O\'qituvchini tajriba yili')



    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    typer = models.CharField(verbose_name='Izoh qoldiruvchi', max_length=150)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Darsni tanlang', null=True)
    likes = models.CharField(max_length=150, verbose_name='Sizga bu darsni nimasi yoqdi', null=True)


    def __str__(self):
        return self.typer

class Student(models.Model):
    user = models.CharField(max_length=150, verbose_name='O\'quvchining ismi')
    age = models.DateField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='O\'quvchi qatnashadigan dars')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,verbose_name='Dars o\'tadigan o\'qituvchi')
    phone_number = models.CharField(max_length=25, verbose_name='O\'quvchining telefon raqami')
    gender = models.CharField(max_length=15, verbose_name='O\'quvchining jinsi', null=True)





    def __str__(self):
        return self.teacher.name




