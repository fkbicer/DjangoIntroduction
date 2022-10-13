from django.db import models
from django.contrib.auth.models import User


# abstract = True diyerek, bu model için veritabanında tablo olusmasını engelledik.
class Company(models.Model):
    name=models.CharField(verbose_name='isim', max_length=100)
    content=models.TextField(verbose_name='aciklama')
    author=models.ForeignKey(User,verbose_name='sahip',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class BookCompany(Company):
    pass

class GameCompany(Company):
    pass

class Book(models.Model):
    name=models.CharField(max_length=100)
    page_count = models.PositiveSmallIntegerField()

class Intro(Book):
    content = models.TextField()

class ProxyBookManager(models.Manager):
    pass

class ProxyBook(Book):

    objects = ProxyBookManager()
    class Meta:
        proxy= True
        ordering =['name']

    def short_name(self):
        return self.name[:10]