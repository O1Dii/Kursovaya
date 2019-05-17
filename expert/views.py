from django.contrib import auth
from django.shortcuts import render
from django.views.generic import View

from manager.models import *
from manager.util import AuthCheckMixin


class ExpertPage(AuthCheckMixin, View):
    def get(self, request):
        perm = self.check_perm_expert(request)
        if perm is not None:
            return perm
        topics = Topic.objects.filter(active=True)
        attrs = {
            'topics': topics
        }
        return render(request, 'expert.html', attrs)


class TopicDetailPage(AuthCheckMixin, View):
    def get(self, request, id):
        perm = self.check_perm_expert(request)
        if perm is not None:
            return perm
        topic = Topic.objects.get(pk=id)
        solutions = Solution.objects.filter(topic=topic)
        attrs = {
            'topic': topic,
            'solutions': solutions
        }
        return render(request, 'topic.html', attrs)

    def post(self, request, id):
        topic = Topic.objects.get(pk=id)
        solutions = Solution.objects.filter(topic=topic)
        attrs = {
            'topic': topic,
            'solutions': solutions
        }
        for i in range(len(solutions)):
            if SolutionRating.objects.get(expert_rating=auth.get_user(request).rating,
                                          solution=solutions[i]) is not None:
                SolutionRating.objects.create(rating=request.POST.get('dec_field' + str(i + 1)),
                                              expert_rating=auth.get_user(request).rating,
                                              solution=solutions[i])
            else:
                sol_rating = SolutionRating.objects.get(expert_rating=auth.get_user(request).rating,
                                                        solution=solutions[i])
                sol_rating.rating = request.POST.get('dec_field' + str(i + 1))
                sol_rating.save()
        return render(request, 'topic.html', attrs)
