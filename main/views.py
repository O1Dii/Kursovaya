from django.contrib import auth
from django.views.generic import View
from django.shortcuts import render, redirect


def main_page(request):
    if auth.get_user(request).id is None:
        return redirect('/auth/login')
    elif bool(auth.get_user(request).is_superuser):
        return redirect('/admin/')
    elif bool(auth.get_user(request).is_staff):
        return redirect('/manager/')
    return redirect('/expert/')


