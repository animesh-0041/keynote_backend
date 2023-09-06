from rest_framework import generics
from .models import StudentCourse
from .serializers import StudentCourseSerializer
from django.http import JsonResponse
class StudentCourseCreateAPIView(generics.CreateAPIView):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer




# get course by instructore
def get_courses(request):
    student_id = request.GET.get('student_id')

    if student_id is not None:
        # If instructor_id is provided, filter courses by instructor_id
        courses = StudentCourse.objects.filter(student_id=student_id)
    else:
        # If instructor_id is not provided, get all courses
        courses = StudentCourse.objects.all()

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
            'student_id': course.student_id,
            'student_name': course.student_name
        }
        for course in courses
    ]

    # Send a JSON response with the course data
    return JsonResponse({'courses': serialized_courses})

