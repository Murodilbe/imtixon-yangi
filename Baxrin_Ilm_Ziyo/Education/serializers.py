from rest_framework import serializers
from .models import  Comment, Teacher, Student, Lesson


# SERIALIZERLAR

class CommentSerializers(serializers.ModelSerializer):
    likes = serializers.ChoiceField(choices=[('option1', 'Like: Yoqdi'), ('option2', 'DisLike: Yoqmadi')])
    class Meta:
        model = Comment
        fields = '__all__'


    def create(self, validated_data):
        likes = validated_data.pop('likes')
        instance = super().create(validated_data)
        instance.likes = likes
        instance.save()
        return instance

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'





class StudentSerializers(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=[('option1', 'Erkak'), ('option2', 'Ayol')])

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        gender = validated_data.pop('gender')
        instance = super().create(validated_data)
        instance.gender = gender
        instance.save()
        return instance


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


