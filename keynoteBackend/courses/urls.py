# courses/urls.py
from django.urls import path
# from .views import CourseCreateAPIView, CourseListAPIView,CourseListByInstructor
from .views import get_courses,CourseCreateAPIView,delete_course,edit_course

urlpatterns = [
    path('create/', CourseCreateAPIView.as_view(), name='course-create'),
    path('',get_courses , name='course-list'),
    path('delete/<int:id>/', delete_course, name='delete-course'),
    path('edit/<int:id>/',edit_course, name='edit-course'),
]
   

