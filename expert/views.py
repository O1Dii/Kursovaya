from django.shortcuts import render
from django.views.generic import View

from manager.models import *
from manager.util import AuthCheckMixin


class ExpertPage(AuthCheckMixin, View):
    def get(self, request):
        perm = self.check_perm_expert(request)
        if perm is not None:
            return perm
        topics = Topic.objects.all()
        attrs = {
            'topics': topics
        }
        return render(request, 'expert.html', attrs)
