from django.urls import path
from . import views
from .views import home, registration, login, dashboard

urlpatterns = [
    path('', home, name='index')
    , path('registration', registration)
    , path('login', login)
    , path('dashboard', dashboard)
]
