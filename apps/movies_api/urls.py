from django.conf.urls import url

from apps.movies_api import views

urlpatterns = [
    url('film/', views.FilmView.as_view()),
    url('cate/', views.CateView.as_view()),
    url('decade/', views.DecadeView.as_view()),
    url('loc/', views.LocView.as_view()),
    url('sub/', views.SubView.as_view()),
    url('type/', views.TypeView.as_view()),
]
