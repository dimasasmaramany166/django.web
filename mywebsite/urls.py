
from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articel/<int:year>/', views.year),
    path('berita/<halaman>/', views.berita),
    path('', views.index, name='index'),
    re_path(r'^(?P<input>[0-9]+)/$', views.page), #re_path digunakan untuk versi lama
    # path('blog/page<int:num>/', views.page),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls'))
]
