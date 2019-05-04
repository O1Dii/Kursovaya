from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Topic, Solution, SolutionRating
from .forms import TopicForm, SolutionFormset


class ManagerPage(View):
    def get(self, request):
        return render(request, 'manager.html', {})


class NewTopicPage(View):
    def get(self, request):
        heading_message = 'Formset Demo'
        if request.method == 'GET':
            formset = SolutionFormset(request.GET or None)
            print(formset)
        elif request.method == 'POST':
            formset = SolutionFormset(request.POST)
            if formset.is_valid():
                for form in formset:
                    # extract name from each form and save
                    name = form.cleaned_data.get('name')
                    # save book instance
                    if name:
                        # Book(name=name).save()
                        pass
                # once all books are saved, redirect to book list view
                return redirect('/manager')
        return render(request, 'new.html', {
            'form': TopicForm,
            'formset': formset,
            'heading': heading_message,
        })


class ResultsPage(View):
    def get(self, request):
        return render(request, 'results.html', {})


class SettingsPage(View):
    def get(self, request):
        return render(request, 'settings.html', {})


class ExpertsPage(View):
    def get(self, request):
        return render(request, 'experts.html', {})


class TopicDetailPage(View):
    def get(self, request, id):
        topic = Topic.objects.get(pk=id)
        solutions = Solution.objects.filter(topic=topic)
        attrs = {
            'topic': topic,
            'solutions': solutions
        }
        return render(request, 'topic.html', attrs)

    def post(self, request, id):
        if request.method == "POST":
            topic = Topic.objects.get(pk=id)
            solutions = Solution.objects.filter(topic=topic)
            attrs = {
                'topic': topic,
                'solutions': solutions
            }
            for i in range(len(solutions)):
                SolutionRating.objects.create(rating=request.POST.get('dec_field' + str(i + 1)),
                                              solution=solutions[i])
        return render(request, 'topic.html', attrs)
