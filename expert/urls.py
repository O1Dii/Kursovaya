from django.urls import path
from .views import *

urlpatterns = (
    path('', ExpertPage.as_view()),
    path('topics/<int:id>', TopicDetailPage.as_view(), name='topics'),
)