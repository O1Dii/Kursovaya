from django import forms

from .models import *


class TopicForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'size': 40,
               'placeholder': 'Название темы'}),
        label='Тема')
    description = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3,
               'placeholder': 'Описание темы'}),
        label="Описание темы")

    class Meta:
        model = Topic
        fields = (
            "name",
            'description'
        )


class ManagerEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = (
            'email',
            'first_name',
            'last_name',
            'organization'
        )


class SolutionForm(forms.ModelForm):
    name = forms.CharField(initial='Решение', widget=forms.TextInput(
        attrs={'size': 40,
               'placeholder': 'Название решения'}),
        label='Решение')
    description = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3,
               'placeholder': 'Описание решения'}),
        label="Описание")
    image = forms.ImageField(label='Изображение для решения', required=False)

    class Meta:
        model = Solution
        fields = (
            "name",
            "description",
            'image',
        )
