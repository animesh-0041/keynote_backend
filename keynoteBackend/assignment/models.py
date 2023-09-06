# assignment/models.py
from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    
    # New fields
    instructor_id = models.PositiveIntegerField()
    instructor_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
    credits = models.PositiveIntegerField()
    department = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
