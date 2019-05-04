from django import forms
from .models import *


class TopicForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))

    class Meta:
        model = Topic
        fields = (
            "name",
            'description'
        )


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = (
            "name",
            "description"
        )


SolutionFormset = forms.formset_factory(SolutionForm, extra=1)
