from django.db import models

class Barang(models.Model):
    namabarang = models.CharField(max_length=255)
    deskripsi = models.TextField()
    hargabeli =models.IntegerField()
    hargajual = models.IntegerField()
    stok = models.IntegerField()
    info = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.namabarang
