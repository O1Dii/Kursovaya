import decimal

from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from .models import UserModel


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    first_name = forms.CharField(label='Имя', max_length=30, required=True, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'name': 'first_name', 'id': 'first_name','placeholder': 'Введите ваше Имя'}))
    last_name = forms.CharField(label='Фамилия', max_length=150, required=True, widget=forms.TextInput(attrs={"type": "text", "class": "form-control", "name": "last_name", 'id': "last_name", 'placeholder':"Введите вашу Фамилию"}))
    rating_i = forms.DecimalField(label='Ra', required=False, max_digits=3, decimal_places=2)
    rating_a = forms.DecimalField(label='Ri', required=False, max_digits=3, decimal_places=2)
    email = forms.EmailField(label="e-mail", max_length=30, required=True, widget=forms.EmailInput(attrs={"type":"text", "class":"form-control", "name":"email", "id":"email", "placeholder":"Введите ваш Email"}))
    organization = forms.CharField(label='Организация', help_text='', required=True, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "name":"organization", "id":"organization", "placeholder":"Введите вашу организацию"}))
    password1 = forms.CharField(label='Пароль', help_text='', required=True, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "name":"password", "id":"password", "placeholder":"Введите пароль"}))
    password2 = forms.CharField(label='Подтверждение пароля:', help_text='', required=True, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "name":"confirm", "id":"confirm", "placeholder":"Подтвердите ввод пароля"}))

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'organization', 'rating_i', 'rating_a', 'password1', 'password2', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        rating_i = self.cleaned_data.get('rating_i')
        rating_a = self.cleaned_data.get('rating_a')
        if rating_a is not None:
            user.rating = decimal.Decimal.from_float((float(rating_i) * 0.1 + float(rating_a)) / 2)
        else:
            user.rating = None

        user.is_staff = False
        user.status = False
        user.is_active = True
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    rating_i = forms.DecimalField(label='Ra', required=False, max_digits=3, decimal_places=2)
    rating_a = forms.DecimalField(label='Ri', required=False, max_digits=3, decimal_places=2)

    class Meta:
        model = UserModel
        fields = 'first_name', 'last_name', 'organization', 'rating_i', 'rating_a'

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        rating_i = self.cleaned_data.get('rating_i')
        rating_a = self.cleaned_data.get('rating_a')
        if rating_a is not None and rating_i is not None:
            user.rating = decimal.Decimal.from_float((float(rating_i) * 0.1 + float(rating_a)) / 2)
        if commit:
            user.save()
        return user


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', help_text='', required=True, widget=forms.PasswordInput(
        attrs={"type": "password", "class": "form-control", "name": "password", "id": "password",
               "placeholder": "Введите старый пароль"}))
    new_password1 = forms.CharField(label='Новый пароль', help_text='', required=True, widget=forms.PasswordInput(
        attrs={"type": "password", "class": "form-control", "name": "password", "id": "password",
               "placeholder": "Введите пароль"}))
    new_password2 = forms.CharField(label='Подтверждение пароля:', help_text='', required=True, widget=forms.PasswordInput(
        attrs={"type": "password", "class": "form-control", "name": "confirm", "id": "confirm",
               "placeholder": "Подтвердите ввод пароля"}))
