from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def login_view(request, *args, **kwargs):
    user = authenticate(request.data.username, request.data.password)
    login(request, user)

    return redirect('/')


@api_view(['POST'])
def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('/')


@api_view(['POST'])
def register_view(request, *args, **kwargs):
    user = User.objects.create_user(username=request.data.username, password=request.data.password)

    login(request, user)

    return redirect('/')
