from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import CustomUser
from .services import is_valid_request, create_user, email_exists, username_exists

# Create your views here.
@api_view(['POST'])
def register(request):
    try:
        if not is_valid_request(request.data):
            return JsonResponse({'error': 'Please provide all required fields.'}, status=400)
        
        email = request.data['email']
        username = request.data['username']

        if email_exists(email):
            return JsonResponse({'error': 'A user with that email already exists.'}, status=400)
        
        if username_exists(username):
            return JsonResponse({'error': 'A user with that username already exists.'}, status=400)
        
        create_user(email, request.data['username'], request.data['password'])
        
        return JsonResponse({'message': 'User registered successfully!'}, status=201)
    
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=500)