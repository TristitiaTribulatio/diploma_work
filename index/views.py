from django.views import View
from django.shortcuts import render, redirect
from .models import Admin, Requests, Codes, Themes
from .forms import AuthForm, RequestForm, StatusForm, CheckCodeForm
from django.contrib.auth.backends import BaseBackend
from datetime import datetime
from random import randint


class MainView(View):
    @staticmethod
    def get(request):
        return render(request, "main.html", {'auth': AuthForm, 'request': RequestForm, 'status': StatusForm})


class AdminView(View):
    @staticmethod
    def get(request):
        try:
            if request.session['admin']:
                requests = ShowRequests.show(Requests.objects.all())
                return render(request, 'admin.html', {'requests': requests})
        except KeyError:
            return redirect('/')


class ViewingRequestsView(View):
    @staticmethod
    def get(request):
        try:
            if request.session['phone']:
                return render(request, 'viewing_requests.html', {'code': False, 'code_form': CheckCodeForm})
            return redirect('/')
        except KeyError:
            return redirect('/')


class AuthView(View):
    @staticmethod
    def post(request):
        login_admin = request.POST['login_admin']
        password_admin = request.POST['password_admin']
        admin = BackendAuth.authenticate(request, login=login_admin, password=password_admin)
        if admin is not None:
            request.session['admin'] = True
            return redirect('/admin_page/')
        return redirect('/')


class RequestView(View):
    @staticmethod
    def post(request):
        name = request.POST['name_request']
        phone = request.POST['phone_request']
        email = request.POST['email_request']
        desc = request.POST['description_request']
        theme = request.POST['themes_request']
        date = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        Requests(name=name, phone=phone, email=email, description=desc, date=date, status_id=1, theme_id=theme).save()
        return redirect('/')


class StatusView(View):
    @staticmethod
    def post(request):
        phone_status = request.POST['phone_status']
        try:
            if Requests.objects.get(phone=phone_status):
                StatusView.phone(request, phone_status)
                return redirect('/view_requests/')
        except Requests.DoesNotExist:
            return redirect('/')
        except Requests.MultipleObjectsReturned:
            StatusView.phone(request, phone_status)
            return redirect('/view_requests/')

    @staticmethod
    def phone(request, phone_status):
        StatusView.delete_code(request)
        request.session['phone'] = phone_status
        Codes(code=str(randint(1000, 9999)), phone=phone_status).save()

    @staticmethod
    def delete_code(request):
        Codes.objects.all().delete()


class CheckCodeView(View):
    @staticmethod
    def post(request):
        code = request.POST['code']
        try:
            if Codes.objects.get(phone=request.session['phone']).code == code:
                requests = ShowRequests.show(Requests.objects.filter(phone=request.session['phone']))
                return render(request, 'viewing_requests.html', {'code': True, 'requests': requests})
            return redirect('/view_requests/')
        except Codes.DoesNotExist:
            return redirect('/view_requests/')


class UpdateValue:
    @staticmethod
    def update(act, id, status):
        if act:
            Requests.objects.filter(id=id).update(status_id=status)


class ShowRequests:
    @staticmethod
    def show(requests_db):
        requests = []
        for req in requests_db:
            requests.append([req.name, req.email, req.phone, Themes.objects.get(id=req.theme_id).theme,
                             req.description, req.date.strftime("%M:%H %m-%d-%Y"), req.status_id, req.id])
        return requests


class AcceptView(View):
    @staticmethod
    def get(request):
        UpdateValue.update(request.GET['act'], request.GET['id'], 2)
        return redirect('/admin_page/')


class RejectView(View):
    @staticmethod
    def get(request):
        UpdateValue.update(request.GET['act'], request.GET['id'], 3)
        return redirect('/admin_page/')


class DoneView(View):
    @staticmethod
    def get(request):
        Requests.objects.filter(id=request.GET['id']).delete()
        return redirect('/admin_page/')


class ResumeView(View):
    @staticmethod
    def get(request):
        UpdateValue.update(request.GET['act'], request.GET['id'], 1)
        return redirect('/admin_page/')


class DeleteView(View):
    @staticmethod
    def get(request):
        if request.GET['act']:
            Requests.objects.filter(id=request.GET['id']).delete()
            return redirect('/admin_page/')
        return redirect('/admin_page/')


class LogoutView(View):
    @staticmethod
    def get(request):
        del request.session['admin']
        return redirect('/')


class BackendAuth(BaseBackend):
    @staticmethod
    def authenticate(request, login=None, password=None):
        try:
            admin = Admin.objects.get(login=login)
            if admin.password == password:
                return admin
            else:
                return None
        except Admin.DoesNotExist:
            return None
