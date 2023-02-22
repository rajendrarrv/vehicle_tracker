from itertools import count
from sqlite3 import IntegrityError
from time import timezone

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from sqlalchemy import null

from polls.models import User
from django.utils import timezone


def home(request):
    if check_session(request):
        return HttpResponseRedirect('dashboard')
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
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    query_set = User.objects.filter(email_text=username).filter(password_text=password)
    if len(query_set) == 0:
        return HttpResponse("User does not exit", content_type='text/plain')
    else:
        user = query_set[0]
        request.session['email'] = user.email_text
        request.session['name'] = user.name_text
        request.session['mobile'] = user.mobile_no_text
        return HttpResponseRedirect('dashboard')


def dashboard(request):
    context = {'name': request.session['name']}

    return render(request, 'polls/dashboard.html', context)


def check_session(request):
    email = request.session.get('email', None)

    return email is not None


def logout(request):
    try:
        del request.session['email']

    except:
        return HttpResponse("Logout is not working", content_type='text/plain')
    return HttpResponseRedirect('/')
