from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sewage_info/', views.sewage_info, name='sewage-info')
]
