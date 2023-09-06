# courses/urls.py
from django.urls import path
# from .views import CourseCreateAPIView, CourseListAPIView,CourseListByInstructor
from .views import StudentCourseCreateAPIView,get_courses

urlpatterns = [
  
    path('create/',StudentCourseCreateAPIView.as_view(), name='post_courses'),
    path('',get_courses, name='get_courses'),
]
   

