from django.urls import path

from .views import *

app_name = 'manager'

urlpatterns = (
    path('', ManagerPage.as_view()),
    path('new/', NewTopicPage.as_view(), name='new'),
    path('results/', ResultsPage.as_view(), name='results'),
    path('results/<int:id>', ResultsDetailPage.as_view(), name='results_detail'),
    path('settings/', SettingsPage.as_view(), name='settings'),
    path('settings/edit', EditManager.as_view(), name='manager_edit'),
    path('experts/', ExpertsPage.as_view(), name='experts'),
    path('experts/<int:id>', ExpertEditPage.as_view(), name='expert_edit'),
)