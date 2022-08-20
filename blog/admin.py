from django.contrib import admin

# Register your models here.
from .models import Post

class adminPost(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ] #menampilkan fiel/data form pada web Admin

admin.site.register(Post, adminPost)