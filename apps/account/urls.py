from django.conf.urls import url

from account import views

urlpatterns = [
    url('register/', views.register, name='register'),
    url('login/', views.login_view, name='login'),
    url('logout/', views.logout_view, name='logout'),
    url('active/', views.active_account),
]
