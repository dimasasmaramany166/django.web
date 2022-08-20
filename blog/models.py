from django.db import models
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    objects = None
    title = models.CharField(max_length=100) #varhcar
    slug = models.SlugField(blank=True, editable=False)
    category = models.CharField(blank=False, max_length=100, default='') #Wajib isi Category
    body = models.TextField(max_length=200) #Text
    email = models.EmailField(default='nama@gmail.com')
    alamat = models.CharField(max_length=200, blank=True) #Blank=True Field Boleh kosong
    waktuPost = models.DateTimeField(auto_now_add=True) #waktu post sekarang

    def save(self):
        self.slug = slugify(self.title) #mengambil nama judul terus akan di save menjadi slug
        super(Post, self).save()

    def __str__(self):
        return "{}. {}".format(self.id, self.title) #menampilkan data pada website admin Djnago