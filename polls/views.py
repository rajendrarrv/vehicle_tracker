from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf


def home(request):
    return render(request, 'polls/index.html')


def registration(request):
    return HttpResponse("this is registration page", content_type='text/plain')


def login(request):
    return HttpResponse("this is login page", content_type='text/plain')
