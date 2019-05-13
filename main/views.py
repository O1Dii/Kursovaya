from django.contrib import auth
from django.shortcuts import redirect


def main_page(request):
    if auth.get_user(request).is_anonymous:
        return redirect('/auth/login')
    elif bool(auth.get_user(request).is_staff):
        return redirect('/admin/')
    elif auth.get_user(request).rating is None:
        return redirect('/manager/')
    return redirect('/expert/')


