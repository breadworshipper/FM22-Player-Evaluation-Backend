from django.contrib.auth.hashers import make_password
from .models import CustomUser

def is_valid_request(data):
    return data.get('email') and data.get('username') and data.get('password')

def create_user(email, username, password):
    user = CustomUser(email=email, username=username, password=make_password(password))
    user.save()
    return user

def email_exists(email):
    return CustomUser.objects.filter(email=email).exists()

def username_exists(username):
    return CustomUser.objects.filter(username=username).exists()
