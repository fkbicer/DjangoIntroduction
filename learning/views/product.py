from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from learning.models import Product
from django.db import transaction


@require_http_methods(['GET', 'POST'])
def product(request, pk=None):
    querySet = Product.objects.get(pk=pk)
    content = {
        'product_detail': querySet
    }
    return render(request=request, template_name='product/detail.html', context=content)


@transaction.atomic
def products(request):
    querySet = Product.objects.all()
    content = {
        'products': querySet
    }
    return render(request=request, template_name='product/list.html', context=content)


def product_archieve(request, year=None, month=None):
    queryset = Product.objects.filter(created__year=year, created__month=month)
    content = {
        'month': month,
        'year': year,
        'products': queryset
    }
    return render(request=request, template_name='product/archieve.html', context=content)
