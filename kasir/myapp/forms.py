from django import forms
from .models import Barang

class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['namabarang', 'deskripsi', 'hargabeli', 'hargajual', 'stok', 'info']
        widgets = {
            'namabarang': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'hargabeli': forms.NumberInput(attrs={'class': 'form-control'}),
            'hargajual': forms.NumberInput(attrs={'class': 'form-control'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
        }
