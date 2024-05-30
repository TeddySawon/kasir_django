from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('kasir/', views.kasir, name='kasir'),
    path('checkout/', views.checkout, name='checkout'),
    
    path('product/', views.product, name='product'),
    path('product/addproduct', views.tambah_barang, name='tambah_barang'),
    path('product/edit/<int:id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
    # path lainnya
]
