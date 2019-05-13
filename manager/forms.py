from django import forms

from .models import *


class TopicForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 40}), label='Тема')
    description = forms.CharField(widget=forms.TextInput(attrs={'size': 40}), label="Описание темы")

    class Meta:
        model = Topic
        fields = (
            "name",
            'description'
        )


class SolutionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 40}), label='Решение')
    description = forms.CharField(label='Описание')

    class Meta:
        model = Solution
        fields = (
            "name",
            "description"
        )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Изображение для решения', required=False)

    class Meta:
        model = SolutionImage
        fields = (
            'image',
        )