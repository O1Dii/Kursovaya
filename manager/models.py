from django.db import models

from loginsys.models import UserModel


class Topic(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(unique=True)
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Solution(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(unique=True)
    image = models.ImageField()
    topic = models.ForeignKey(Topic, blank=True, null=True, default=None, on_delete=None)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'


class SolutionRating(models.Model):
    rating = models.DecimalField(decimal_places=0, max_digits=2)
    expert_rating = models.DecimalField(decimal_places=2, max_digits=3)
    solution = models.ForeignKey(Solution, blank=True, null=True, default=None, on_delete=None)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class ExpertsToTopics(models.Model):
    expert = models.ForeignKey(UserModel, on_delete=None)
    topic = models.ForeignKey(Topic, on_delete=None)

    class Meta:
        verbose_name = 'Связь эксперт-вопрос'
        verbose_name_plural = 'Связи эксперт-вопрос'
