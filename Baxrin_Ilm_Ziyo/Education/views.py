from email.message import EmailMessage

from rest_framework.views import APIView
from django.http import HttpResponse

from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render, redirect
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import LessonSerializers,TeacherSerializers,CommentSerializers,StudentSerializers
from rest_framework import viewsets,permissions
from .models import Lesson,  Teacher, Student, User,Comment

# Create your views here.
class LessonView(viewsets.ModelViewSet):
    serializer_class = LessonSerializers
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]


    def get_queryset(self):
        return Lesson.objects.all()


# LIKE QISMI


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializers
    permission_classes = [permissions.DjangoModelPermissions]

    def get_queryset(self):
        return Student.objects.all()


class TeacherView(viewsets.ModelViewSet):
    serializer_class = TeacherSerializers
    permission_classes = [permissions.DjangoModelPermissions]

    def get_queryset(self):
        return Teacher.objects.all()


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    permission_classes = [permissions.DjangoModelPermissions]

    def get_queryset(self):
        return Comment.objects.all()


'''SEARCH QISMI'''




class SearchView(APIView):
    def search(self, request: Request):
        word = request.query_params.get('word')
        lesson = Lesson.objects.filter(name__icontains='word')
        return Response(LessonSerializers(lesson,many=True).data)






# EMAil qismi
from django.core.mail import send_mail
from django.conf import settings
from Baxrin_Ilm_Ziyo import settings
from django.http import HttpRequest, HttpResponse


def send_email(request):
        if request.method == 'POST':
            name = request.POST['name']
            sender_email = request.POST['email']
            msg = request.POST['msg']
            phone = request.POST['phone']



            email = EmailMessage(
                settings.EMAIL_HOST_USER,


            )
            email.fail_silently = True
            return HttpResponse('Muvaffaqiyatli jo\'tildi')
        return render(request, 'Education/email.html')



