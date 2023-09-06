from django.http import JsonResponse
from .models import Course  # Import your Course model

from .serializers import CourseSerializer
from rest_framework import generics
from rest_framework import status
from django.shortcuts import get_object_or_404
import json
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import DestroyAPIView 


from .serializers import CourseSerializer

class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



# get course by instructore
def get_courses(request):
    instructor_id = request.GET.get('instructor_id')

    if instructor_id is not None:
        # If instructor_id is provided, filter courses by instructor_id
        courses = Course.objects.filter(instructor_id=instructor_id)
    else:
        # If instructor_id is not provided, get all courses
        courses = Course.objects.all()

    # Serialize the course data to JSON
    serialized_courses = [
        {
            'course_name': course.course_name,
            'department': course.department,
            'credits': course.credits,
            'description': course.description,
            'instructor_name': course.instructor_name,
            'instructor_id': course.instructor_id,
            'course_code': course.course_code,
            'id': course.id
        }
        for course in courses
    ]

    # Send a JSON response with the course data
    return JsonResponse({'courses': serialized_courses})




@api_view(['DELETE'])
def delete_course(request, id):
    try:
        course = Course.objects.get(id=id)
        course.delete()
        return Response({'message': 'Course deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# edit
@api_view(['PATCH'])
def edit_course(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Course edited successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 