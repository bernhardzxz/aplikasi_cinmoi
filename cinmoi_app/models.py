from django.db import models

# Create your models here.
class Menu(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.nama