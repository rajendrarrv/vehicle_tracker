from itertools import count
from sqlite3 import IntegrityError
from time import timezone

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sqlalchemy import null

from polls.models import User
from django.utils import timezone
from django.http import JsonResponse


def home(request):
    # if check_session(request):
    #     return HttpResponseRedirect('dashboard')
    return render(request, 'polls/index.html')


@csrf_exempt
def registration(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    mobile_no = request.POST.get("mobile_no", "")
    password = request.POST.get("password", "")

    try:
        user = User(name_text=name, email_text=email, mobile_no_text=mobile_no, password_text=password,
                    pub_date=timezone.now())
        user.save()

        msg = '{"data": "record is saved successfully", "error": {}}'
        response = JsonResponse(msg)

        HttpResponse(response.content, content_type='text/plain')
    except Exception as e:
        msg = "user is already exist"
        msg = '{"data": {}, "error": e}'
        response = JsonResponse(msg)

        return HttpResponse(response.content, content_type='text/plain')
    return HttpResponse(msg, content_type='text/plain')


def message(request, title, message):
    context = {'title': title, 'message': message}
    return render(request, 'polls/message.html', context)


@csrf_exempt
def login(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    query_set = User.objects.filter(email_text=username).filter(password_text=password)
    if not query_set.exists():
        msg = {"error": "something is going wrong"}
        response = JsonResponse(msg)
        return HttpResponse(response.content, content_type='text/plain')
    else:
        user = query_set[0]
        msg = {"data": {"email": user.email_text, "name": user.name_text, "mobile": user.mobile_no_text}, "error": {}}
        response = JsonResponse(msg)
    return HttpResponse(response.content, content_type='text/plain')


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
