from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]
    
    TYPE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor')
    ]

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    department = models.CharField(max_length=255)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
