from django import forms
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from loginsys.forms import UserEditForm
from loginsys.models import UserModel
from .forms import TopicForm, SolutionForm, ManagerEditForm
from .models import Topic, Solution, SolutionRating, ExpertsToTopics
from .util import AuthCheckMixin


class ManagerPage(AuthCheckMixin, View):
    def get(self, request):
        perm = self.check_perm_manager(request)
        if perm is not None:
            return perm
        return render(request, 'manager.html', {})


class NewTopicPage(AuthCheckMixin, View):
    def get(self, request):
        experts = UserModel.objects.filter(is_staff=False).exclude(rating=None)
        perm = self.check_perm_manager(request)
        if perm is not None:
            return perm
        SolutionFormset = forms.formset_factory(SolutionForm, extra=2)
        formset = SolutionFormset(request.GET or None)
        return render(request, 'new.html', {
            'form': TopicForm,
            'formset': formset,
            'id': id,
            'experts': experts
        })

    def post(self, request):
        SolutionFormset = forms.formset_factory(SolutionForm, extra=2)
        experts = UserModel.objects.filter(is_staff=False).exclude(rating=None)
        formset = SolutionFormset(request.POST, request.FILES)
        topic_form = TopicForm(request.POST)
        print(formset.is_valid())
        if formset.is_valid() and topic_form.is_valid():
            topic = topic_form.save()
            for i in range(len(experts)):
                if request.POST.get('expert' + str(i)):
                    ExpertsToTopics.objects.create(expert=experts[i], topic=topic)
            for form in formset:
                Solution.objects.create(**form.cleaned_data, topic=topic)
        else:
            return render(request, 'new.html', {'form': topic_form,
                                                'formset': formset,
                                                'id': id,
                                                'experts': experts,
                                                'error': True})
        return redirect('/manager')


class ResultsPage(AuthCheckMixin, View):
    def get(self, request):
        perm = self.check_perm_manager(request)
        if perm is not None:
            return perm
        topics = Topic.objects.filter(active=True)
        topics_sec = Topic.objects.filter(active=False)
        attrs = {
            'topics': topics,
            'topics_sec': topics_sec
        }
        return render(request, 'results.html', attrs)


class ResultsDetailPage(AuthCheckMixin, View):
    def get(self, request, id):
        perm = self.check_perm_manager(request)
        if perm is not None:
            return perm
        topic = Topic.objects.get(id=id)
        solutions = Solution.objects.filter(topic=topic)
        ratings = []
        for solution in solutions:
            solution_ratings = SolutionRating.objects.filter(solution=solution)
            expert_ratings_sum = sum([i.expert_rating for i in solution_ratings])
            temp_solution_ratings = []
            for i in range(len(solution_ratings)):
                temp_solution_ratings.append(solution_ratings[i].rating
                                             * solution_ratings[i].expert_rating
                                             / expert_ratings_sum)
            w = sum(temp_solution_ratings)
            ratings.append([solution.name, w])

        ratings_sum = sum([i[1] for i in ratings])
        if ratings_sum != 0:
            for i in range(len(ratings)):
                ratings[i][1] = float(round(ratings[i][1] / ratings_sum, 2))
        else:
            ratings.clear()

        print(ratings)
        attrs = {
            'ratings': ratings,
            'topic': topic.name,
            'topic_active': topic.active,
            'page_id': id
        }
        return render(request, 'results_detail.html', attrs)

    def post(self, request,  id):
        # if request.POST.get('delete') is not None:
        topic = Topic.objects.get(id=id)
        topic.active = False
        topic.save()
        return redirect('/manager/results')


class SettingsPage(AuthCheckMixin, View):
    def get(self, request):
        perm = self.check_perm_manager(request)
        if perm is not None:
            return perm
        return render(request, 'settings.html', {})


class ExpertsPage(AuthCheckMixin, View):
    def get(self, request):
        perm = self.check_perm_manager(request)
        if perm is not None:
            return perm
        experts = UserModel.objects.filter(is_staff=False).exclude(rating=None)
        return render(request, 'experts.html', {'experts': experts})


class ExpertEditPage(AuthCheckMixin, View):
    def get(self, request, id):
        perm = self.check_perm_manager(request)
        if perm is not None:
            return perm
        expert = UserModel.objects.get(sys_id=id)
        form = UserEditForm(instance=expert)
        return render(request, 'expert_edit.html', {'form': form, 'page_id': id, 'expert_email': expert.email})

    def post(self, request, id):
        expert = UserModel.objects.get(sys_id=id)
        if request.POST.get('delete') is not None:
            expert.delete()
        else:
            form = UserEditForm(request.POST, instance=expert)
            form.save()
        return redirect('/')


class EditManager(View):
    def get(self, request):
        return render(request, 'manager_edit.html', {'form': ManagerEditForm(instance=request.user)})

    def post(self, request):
        form = ManagerEditForm(request.POST, instance=request.user)
        form.save()
        return redirect('/')
