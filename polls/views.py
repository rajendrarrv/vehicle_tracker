from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf


def home(request):
    return render(request, 'polls/index.html')


def registration(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    mobile_no = request.POST.get("mobile_no", "")
    print("Name " + name + "\nEmail " + email + "\nMobile no " + mobile_no)
    return HttpResponse("this is registration page", content_type='text/plain')


def login(request):
    return HttpResponse("this is login page", content_type='text/plain')
