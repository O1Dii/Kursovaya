from django.contrib import auth
from django.shortcuts import render


class AuthCheckMixin:
    def check_perm_manager(self, request):
        if auth.get_user(request).rating is not None:
            return render(request, 'access_deny.html', {})

    def check_perm_expert(self, request):
        if auth.get_user(request).rating is None:
            return render(request, 'access_deny.html', {})
