from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserSignUp.as_view(), name='register'),
]