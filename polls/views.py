from time import timezone

from django.http.response import HttpResponse
from django.shortcuts import render
from polls.models import User
from django.utils import timezone


def home(request):
    return render(request, 'polls/index.html')


def registration(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    mobile_no = request.POST.get("mobile_no", "")
    password = request.POST.get("password", "")
    user = User(name_text=name, email_text=email, mobile_no_text=mobile_no, password_text=password,
                pub_date=timezone.now())
    user.save()
    return HttpResponse("this is registration page", content_type='text/plain')


def login(request):
    return HttpResponse("this is login page", content_type='text/plain')
