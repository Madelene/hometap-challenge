from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^properties', views.home, name='home'),
    url(r'^sewage_info', views.sewage_info, name='sewage-info')
]
