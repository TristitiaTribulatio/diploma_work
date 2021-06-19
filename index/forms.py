from django import forms
from .models import Themes

THEMES = []
[THEMES.append([item.id, item.theme]) for item in Themes.objects.all()]


class AuthForm(forms.Form):
    login_admin = forms.CharField(label='', widget=forms.TextInput(
        attrs={'id': 'login', 'placeholder': 'Введите логин', 'required': True}))
    password_admin = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'id': 'pass', 'placeholder': 'Введите пароль', 'required': True}))


class RequestForm(forms.Form):
    name_request = forms.CharField(label='',  widget=forms.TextInput(
        attrs={'id': 'name', 'placeholder': 'Введите имя', 'required': True}))
    phone_request = forms.CharField(label='',  widget=forms.TextInput(
        attrs={'id': 'phone', 'placeholder': 'Введите номер телефона', 'required': True}))
    email_request = forms.CharField(label='', widget=forms.EmailInput(
        attrs={'id': 'email', 'placeholder': 'Введите эл. почту', 'required': True}))
    themes_request = forms.CharField(label='', widget=forms.Select(choices=THEMES, attrs={'id': 'themes'}))
    description_request = forms.CharField(label='', widget=forms.Textarea(
        attrs={'id': 'desc', 'placeholder': 'Подробно опишите причину заявки', 'required': True}))


class StatusForm(forms.Form):
    phone_status = forms.CharField(label='', widget=forms.TextInput(
        attrs={'id': 'phone_status', 'placeholder': 'Введите номер телефона', 'required': True}))


class CheckCodeForm(forms.Form):
    code = forms.CharField(label='', widget=forms.TextInput(
        attrs={'id': 'code', 'placeholder': 'Введите код', 'required': True}))