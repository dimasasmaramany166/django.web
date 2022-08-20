from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     content = {
      'halaman' : "Halaman Home"
     }
     return render(request, 'index.html',content)

def page(request, input) :
     # return render(request, 'page.html')
     heading = "<h1>Halaman page</h1>"
     str = heading + input
     return HttpResponse(str)

def year(request,year):
     heading = "Halaman Tahun ",year
     str = heading
     return HttpResponse(str)

def berita(request,halaman):
     str = "<h1>{}</h1>".format(halaman)
     return HttpResponse(str)