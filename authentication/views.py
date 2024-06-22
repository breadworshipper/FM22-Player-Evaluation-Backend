from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import CustomUser
from django.contrib.auth.hashers import make_password

# Create your views here.
@api_view(['POST'])
def register(request):
    try:
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')

        if not email or not username or not password:
            return JsonResponse({'error': 'Please provide all required fields.'}, status=400)
        
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'error': 'A user with that email already exists.'}, status=400)
        
        # Create a new user
        user = CustomUser(
            email=email,
            username=username,
            password=make_password(password),  # Hash the password
        )
        user.save()
        
        return JsonResponse({'message': 'User registered successfully!'}, status=201)
    
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=500)