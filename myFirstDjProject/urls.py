from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views
#from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', auth_views.logout, name='logout'),


]
