from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^properties', views.home, name='home')
]
