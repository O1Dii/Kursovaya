# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if bool(auth.get_user(request).is_superuser):
                return redirect('/admin/')
            elif bool(auth.get_user(request).is_staff):
                return redirect('/manager/')
            return redirect('/expert/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'login.html', args)

    else:
        return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', args)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {
            'form': form
        }
        return render(request, 'change_password.html', args)
