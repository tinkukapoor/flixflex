from django.shortcuts import render
from django.shortcuts import render,render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.

def home(request):
    return render_to_response("index.html")

def login(request):
    return render_to_response("loggedin.html")

def logout(request):
    return render_to_response("logout.html")

def register_user(request):
    return render_to_response("register.html")

def invalid_login(request):
    return render_to_response("invalid_login")

def register_success(request):
    return render_to_response("register_success.html")

def aboutus(request):
    return render_to_response("image.html")

def cancel(request):
    return render_to_response("cancel.html")

def services(request):
    return render_to_response("service.html")

def information(request):
    return render_to_response("information.html")

 
