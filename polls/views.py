from sqlite3 import IntegrityError
from time import timezone

from django.http.response import HttpResponse
from django.shortcuts import render
from polls.models import User
from django.utils import timezone


def home(request):
    return render(request, 'polls/index.html')


def registration(request):
    msg = "this is registration page"
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    mobile_no = request.POST.get("mobile_no", "")
    password = request.POST.get("password", "")
    confirm_password = request.POST.get("confirm_password", "")

    if password != confirm_password:
        msg = "Please confirm the password properly"
        return HttpResponse(msg, content_type='text/plain')

    try:
        user = User(name_text=name, email_text=email, mobile_no_text=mobile_no, password_text=password,
                    pub_date=timezone.now())
        user.save()
    except Exception as e:
        msg = "user is already exist"
        return HttpResponse(msg + str(e), content_type='text/plain')
    return HttpResponse(msg, content_type='text/plain')


def login(request):
    return HttpResponse("this is login page", content_type='text/plain')
