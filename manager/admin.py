from django.contrib import admin
from .models import *


class SolutionImageInline(admin.TabularInline):
    model = SolutionImage
    extra = 1


class SolutionInline(admin.TabularInline):
    model = Solution
    extra = 1


class TopicAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Topic._meta.fields]
    inlines = [SolutionInline]

    class Meta:
        model = Topic


admin.site.register(Topic, TopicAdmin)


class SolutionAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Solution._meta.fields]
    inlines = [SolutionImageInline]

    class Meta:
        model = Solution


admin.site.register(Solution, SolutionAdmin)


class SolutionImageAdmin(admin.ModelAdmin):
    list_display = [i.name for i in SolutionImage._meta.fields]

    class Meta:
        model = SolutionImage


admin.site.register(SolutionImage, SolutionImageAdmin)


class RatingsAdmin(admin.ModelAdmin):
    list_display = [i.name for i in SolutionRating._meta.fields]

    class Meta:
        model = SolutionRating


admin.site.register(SolutionRating, RatingsAdmin)
