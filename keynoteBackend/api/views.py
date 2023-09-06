from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



# # get profile
def get_profile(request):
    id = request.GET.get('id')

    if id is not None:
        # If instructor_id is provided, filter courses by instructor_id
        profile = UserProfile.objects.filter(id=id)
    else:
        # If instructor_id is not provided, get all courses
        profile = UserProfile.objects.all()

    # Serialize the course data to JSON
    serialized_courses = [
        {
            'name': profile.name,
            'gender': profile.department,
            'email': profile.credits,
            'dob': profile.description,
            'department': profile.instructor_name,
            'contact_number': profile.instructor_id,
            'course_code': profile.course_code,
            'id': profile.id
        }
        for course in profile
    ]

    # Send a JSON response with the course data
    return JsonResponse({'courses': serialized_courses})







