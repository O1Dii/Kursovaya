from django.urls import path, include
from .views import *

urlpatterns = (
    path('', main_page),
    path('expert/', include('expert.urls')),
    path('manager/', include('manager.urls')),
)
