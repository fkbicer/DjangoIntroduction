from django.contrib import admin
from learning.models import Product


class ProductAdmin(admin.ModelAdmin):
    # fields = ('name', 'content',) # Ürünün içerisinde gözükecek alanlar.
    # readonly_fields = ('content',)
    fieldsets = (
        ('Zorunlu', {'fields': ('name', 'content')},
         ),
        ('Opsiyonel', {
            'fields': ('price', 'stock_count'),
            'classes': ('collapse',) # Ayırdğımız bölümü gizlemek icin (gizle-göster seceneği cıkıyor.)
        })
    )  # Data içerisinde bölümlere ayırmak için.

    exclude = ('slug',)  # Ürünün icerisinde gösterilmeyecek alanlar
    list_display = ('name', 'created', 'author')  # objelerin listelendiği kısımda hangi alanların gösterileceği
    list_filter = ('created',)


# Register your models here.

# admin.site.site_header= 'STOK YÖNETİM PANELİ'
# admin.site.site_title = 'bir stok yönetimi'
# admin.site.index_title = 'Stok Yönetimi'

admin.site.register(Product, ProductAdmin)
