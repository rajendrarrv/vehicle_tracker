from django.urls import path
from . import views
from .views import home, registration, login

urlpatterns = [
    path('', home, name='index')
    , path('registration', registration)
    , path('login', login)
]
