from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import itertools


class ProductManager(models.Manager):
    def active_products(self):
        return self.filter(activa=1)


class Product(models.Model):
    # items = models.Manager()
    # items = ProductManager()
    name = models.CharField(max_length=100,
                            verbose_name='ürün ismi',  #
                            default='standart ürün',  # eğer ki değeri boş olursa defauklt değer basılır.
                            blank=False,
                            null=True,
                            db_index=True,
                            db_column='isim',
                            help_text='ürün ismi için tam açıklayıcı metin')
    content = models.TextField(verbose_name='ürün acıklamasi', max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    stock_count = models.PositiveSmallIntegerField(verbose_name='stok adedi')
    price = models.DecimalField(verbose_name='ürün fiyatı', decimal_places=2, max_digits=10)
    slug = models.SlugField(unique=True, editable=False)  # url'ler için kullanılır, unique olması gerekir.
    author = models.ForeignKey(User, verbose_name='Sahip', on_delete=models.CASCADE)

    class Meta:
        db_table = 'urunler'
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/learning/product/detail/%i' % self.id

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.id:
            self.slug= slugify(self.name)
            
            for slug_id in itertools.count(1):
                if not Product.objects.filter(slug=self.slug).exist():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)
        
        super(Product, self).save()

    @property  # sınıflarımızdaki methodlarımızın property gibi çalışmasını sağlayan decorator
    def summary(self):
        return self.content[:50]
