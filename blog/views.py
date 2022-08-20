from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    data = Post.objects.all()
    content = {
        'halaman' : 'Halaman Blog',
        'posts': data
    }
    return render(request, 'blog/index.html',content)
    # return HttpResponse('Halaman Blog')

def category(request, slugData):
    data = Post.objects.filter(title=slugData)
    # str = data
    print(data)
    return HttpResponse('data')

def slug(request,sluginput) :
    data = Post.objects.get(slug=sluginput)
    #tanda "{}" digunakan untuk menampilkan data
    # title = "judul :{}<br>".format(data.title)
    # slug = "slug : {}<br>".format(data.slug)
    # body = "{}".format(data.body)
    # return HttpResponse(title + slug + body)
    content = {
        'halaman' : 'detail {}'.format(data.title),
        'posts' : data
    }
    return render(request, 'blog/detail.html', content)

def categoryPost(request, categoryData):
    data = Post.objects.filter(category=categoryData)
    categories = Post.objects.values('category').distinct() #menampilkan data yang uniqe atau hanya menampilkan 1 data categories agar tidak terlihat banyaj
    # print(categories)
    content = {
        'halaman' : 'category',
        'posts' : data,
        'categories' : categories
    }
    return render(request, 'blog/category.html', content)
