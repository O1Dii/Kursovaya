from django.urls import path
from .views import *

app_name = 'manager'

urlpatterns = (
    path('', ManagerPage.as_view()),
    path('new/', NewTopicPage.as_view(), name='new'),
    path('results/', ResultsPage.as_view(), name='results'),
    path('settings/', SettingsPage.as_view(), name='settings'),
    path('experts/', ExpertsPage.as_view(), name='experts'),
    path('topics/<int:id>', TopicDetailPage.as_view(), name='topics'),
)