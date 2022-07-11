from django.shortcuts import render, HttpResponse, redirect
from .models import Users, PermissionGroup, Permissions
from .services import init_permission


def login(request):
    if request.method == "GET":
        return HttpResponse("login")

    username = request.POST.get('username')
    passwd = request.POST.get("password")

    user = Users.objects.filter(username=username, password=passwd).first()
    if user:
        request = init_permission.init_user(user, request)
    return redirect('/login')


def home(request):
    return HttpResponse("home")
