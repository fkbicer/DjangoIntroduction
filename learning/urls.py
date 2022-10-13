#learning urls burada yazılacak

from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.products, name='product-list'),
    path('product/detail/<int:pk>/', views.product, name='product-detail'),
    path('product/archieve/<int:year>/<int:month>', views.product_archieve, name ='product-archieve')
]