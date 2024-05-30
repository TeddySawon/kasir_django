from django.shortcuts import render, redirect, get_object_or_404
from .models import Barang
from .forms import BarangForm
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')
    
def kasir(request):
    barangs = Barang.objects.all()
    return render(request, 'kasir.html',{'barangs': barangs})

def checkout(request):
    if request.method == 'POST':
        cart = request.POST.getlist('cart[]')
        for item in cart:
            id, quantity = item.split(',')
            barang = Barang.objects.get(id=id)
            barang.stok -= int(quantity)
            barang.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

    
def product(request):
    barangs = Barang.objects.all()
    data = {
        'barangs':barangs
    }    
    return render(request, 'product.html',data)

def tambah_barang(request):
    if request.method == 'POST':
        form = BarangForm(request.POST)
        if form.is_valid():
            try:  
                form.save()
                return redirect('product')
            except:  
                pass
    else:
        form = BarangForm()
    return render(request, 'tambah_barang.html', {'form': form})


def edit_product(request, id):
    barang = get_object_or_404(Barang, id=id)
    if request.method == 'POST':
        form = BarangForm(request.POST, instance=barang)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = BarangForm(instance=barang)
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, id):
    barang = get_object_or_404(Barang, id=id)
    if request.method == 'POST':
        barang.delete()
        return redirect('product')
    return render(request, 'delete_product.html', {'barang': barang})

