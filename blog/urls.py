from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index),
    # path('android/', views.android),
    # path('web/', views.web),
    # re_path(r'^(?P<slugData>[\w-]+)/$', views.category),
    # re_path(r'^post/(?P<sluginput>[\w-]+)/$', views.slug),
    path('post/<slug:sluginput>/', views.slug),
    # re_path(r'^category/(?P<categoryData>[\w-]+)/$', views.categoryPost),
    path('category/<categoryData>/', views.categoryPost, name='category'),
]