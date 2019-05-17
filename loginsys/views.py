# -*- coding: utf-8 -*-

from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from loginsys.forms import UserCreationForm, ChangePasswordForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            if bool(auth.get_user(request).is_staff):
                return redirect('/admin/')
            elif auth.get_user(request).rating is None:
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
            # newuser = auth.authenticate(email=newuser_form.cleaned_data['email'],
            #                             password=newuser_form.cleaned_data['password2'])
            # auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', args)


def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=request.user)
        args = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'change_password.html', args)
    else:
        form = ChangePasswordForm(user=request.user)
        args = {
            'form': form
        }
        return render(request, 'change_password.html', args)
