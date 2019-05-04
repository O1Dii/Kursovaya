from django.urls import path
from loginsys.views import *

app_name = 'loginsys'

urlpatterns = (
    path('login/', login, name='login'),
    # path('change_log/', change_login, name='change_login'),
    path('change_password/', change_password, name='change_password'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
)