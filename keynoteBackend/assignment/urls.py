from django.urls import path
from .views import create_assignment

urlpatterns = [
    # Other URL patterns
    path('create/', create_assignment, name='create_assignment'),
]
