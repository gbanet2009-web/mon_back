from rest_framework import serializers
from .models import User, Course, Exercise, BacSubject

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'class_id', 'credits')
        read_only_fields = ('id',)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'pdf_url', 'class_id')
        read_only_fields = ('id',)

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'subject', 'title', 'pdf_url', 'class_id')
        read_only_fields = ('id',)

class BacSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BacSubject
        fields = ('id', 'subject', 'title', 'pdf_url')
        read_only_fields = ('id',)
