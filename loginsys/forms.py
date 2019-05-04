from django import forms
from .models import UserModel


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    first_name = forms.CharField(label='Имя', max_length=30, required=True, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'name': 'first_name', 'id': 'first_name','placeholder': 'Enter your Name'}))
    last_name = forms.CharField(label='Фамилия', max_length=150, required=True, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "name":"last_name", 'id':"last_name", 'placeholder':"Enter your surname"}))
    email = forms.EmailField(label="e-mail", max_length=30, required=True, widget=forms.EmailInput(attrs={"type":"text", "class":"form-control", "name":"email", "id":"email", "placeholder":"Enter your Email"}))
    Organization = forms.CharField(label='Организация', help_text='', required=True, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "name":"Organization", "id":"Organization", "placeholder":"Enter your Organization"}))
    password1 = forms.CharField(label='Пароль', help_text='', required=True, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "name":"password", "id":"password", "placeholder":"Введите пароль"}))
    password2 = forms.CharField(label='Подтверждение пароля:', help_text='', required=True, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "name":"confirm", "id":"confirm", "placeholder":"Подтвердите ввод пароля"}))

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'is_active', 'Organization', 'password1', 'password2', 'email')

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
        user.is_staff = False
        user.status = False
        user.is_active = True
        if commit:
            user.save()
        return user
