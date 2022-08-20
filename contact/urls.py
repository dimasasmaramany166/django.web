from django.conf.locale import vi
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
]