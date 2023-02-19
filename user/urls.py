from django.urls import path,include
from .views import *
urlpatterns = [
    path('register',sign_up,name='register'),
    path('login', sign_in, name='login'),
    path('logout', log_out, name='logout'),
]