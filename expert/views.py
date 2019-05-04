from django.views.generic import View
from django.shortcuts import render
from manager.models import *


class ExpertPage(View):
    def get(self, request):
        topics = Topic.objects.all()
        attrs = {
            'topics': topics
        }
        return render(request, 'expert.html', attrs)
