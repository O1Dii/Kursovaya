from django.urls import path
from loginsys.views import login, logout, register

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
]