# courses/models.py
from django.db import models
class StudentCourse(models.Model):
    course_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    credits = models.PositiveIntegerField()
    description = models.TextField()
    course_code = models.CharField(max_length=10, unique=True)
    instructor_name = models.CharField(max_length=255)
    instructor_id = models.PositiveIntegerField()
    student_name = models.CharField(max_length=255)
    student_id = models.PositiveIntegerField()
    

    
    def __str__(self):
      
        return self.course_name
     
