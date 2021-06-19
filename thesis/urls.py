from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from index.views import MainView, AdminView, AuthView, RequestView, StatusView,\
    ViewingRequestsView, CheckCodeView, LogoutView, AcceptView, RejectView, DoneView, ResumeView, DeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('auth/', AuthView.as_view()),
    path('request/', RequestView.as_view()),
    path('status/', StatusView.as_view()),
    path('admin_page/', AdminView.as_view()),
    path('view_requests/', ViewingRequestsView.as_view()),
    path('code/', CheckCodeView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('accept/', AcceptView.as_view()),
    path('reject/', RejectView.as_view()),
    path('done/', DoneView.as_view()),
    path('resume/', ResumeView.as_view()),
    path('delete/', DeleteView.as_view()),
]

urlpatterns += static(settings.STATIC_URL)
