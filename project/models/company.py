import itertools

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Company(models.Model):
    name = models.CharField(max_length=35, verbose_name='isim'),
    content = models.TextField(verbose_name='icerik'),
    address = models.TextField(verbose_name='adres'),
    phone = models.CharField(verbose_name='numara'),
    email = models.EmailField(verbose_name='email'),
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Yetkili')
    created = models.DateTimeField(verbose_name='tarih'),
    active = models.BooleanField(verbose_name='aktiflik')
    slug = models.CharField(verbose_name='Slug', max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.id:
            self.slug = slugify(self.name)

            for slug_id in itertools.count(1):
                if not self.__class__.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)

        super(Company, self).save()
