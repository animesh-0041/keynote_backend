from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Wrong credentials'}, status=401)
