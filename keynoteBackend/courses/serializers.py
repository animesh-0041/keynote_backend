# courses/serializers.py
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'department', 'credits', 'description','course_code','instructor_name','instructor_id','id']