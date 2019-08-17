from django import forms
from .models import User
import re
from django.contrib.auth import authenticate


def password_validator(password: str):

    if not 8 < len(password) < 32:
        raise forms.ValidationError('Длина пароля должна быть от 8 до 32 символов включительно')

    elif not re.findall(r'[A-Z]', password):
        raise forms.ValidationError('Пароль должен содержать заглавные символы')

    elif not re.findall(r'\d', password):
        raise forms.ValidationError('Пароль должен содержать числовые символы')

    elif re.findall(r'\W', password):
        raise forms.ValidationError('Пароль не должен содержать специальные символы')

    return password


def name_validator(name):
    if name and len(name) < 41:

        name_pattern = r'^[A-Za-z0-9][A-Za-z0-9_]+$'

        if re.findall(name_pattern, name):

            if name.endswith('_'):
                raise forms.ValidationError('Имя не должно заканчиваться на _')

            try:  # своеобразная проверка уникальности
                User.objects.get(name=name)
            except User.DoesNotExist:
                return name

            raise forms.ValidationError('Имя пользователя должно быть уникальным')

        raise forms.ValidationError('Имя должно начинаться с [A-Za-z0-9], содержать символы [A-Za-z0-9_]')

    raise forms.ValidationError('Длина имени пользователя должна быть  0 - 40 символ')


def password_field():
    return forms.CharField(max_length=31,widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):

    password = password_field()

    class Meta:
        model = User
        fields = ['name', 'email']

    def clean_password(self):
        return password_validator(self.cleaned_data['password'])

    def clean_name(self):
        return name_validator(self.cleaned_data['name'])


class LoginForm(forms.Form):
    name = forms.CharField(max_length=40)
    password = password_field()

    def clean_password(self):
        password = self.cleaned_data['password']
        name = self.cleaned_data.get('name')

        log_user = authenticate(name=name, password=password)
        if log_user is not None:
            if not log_user.is_active:
                raise forms.ValidationError('Ваш аккаунт был заблокирован')

            elif not log_user.activated:
                raise forms.ValidationError('Подтвердите свой email, прежде чем авторизоваться')

            self.log_user = log_user
            return password

        raise forms.ValidationError('Неверный логин или пароль')


class ResetForm(forms.Form):

    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.get_or_none(email=email)
        if not user or not user.activated:
            raise forms.ValidationError('Пользователя с таким email адрессом не существует')

        elif user.activate_key:
            raise forms.ValidationError('Email письмо уже было отправлено! Проверьте почту или спам')

        return email


class NewPasswordForm(forms.Form):
    password = password_field()
    password2 = password_field()

    def clean_password(self):
        return password_validator(self.cleaned_data['password'])

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data['password2']

        if password == password2:
            return password2

        raise forms.ValidationError('Пароли не совпали')
