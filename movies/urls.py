from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    # url('^$',views.index),
    url('admin/', admin.site.urls),
    url('api/', include('apps.movies_api.urls')),
    url('account/', include('apps.account.urls')),
]
