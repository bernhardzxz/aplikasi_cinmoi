from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    # Definisikan pilihan untuk tipe rasa
    TIPE_RASA_CHOICES = [
        ('manis', 'Manis'),
        ('asin', 'Asin'),
        ('pedas', 'Pedas'),
    ]

    # Definisikan pilihan untuk kategori
    KATEGORI_CHOICES = [
        ('main_course', 'Main Course'),
        ('side_dish', 'Side Dish'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    ]
    
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='menu_images/')
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)  # Menggunakan choices untuk kategori
    tipe_rasa = models.CharField(max_length=50, choices=TIPE_RASA_CHOICES)  # Menggunakan choices untuk tipe rasa
    class Menu(models.Model):TIPE_RASA_CHOICES = [
        ('manis', 'Manis'),
        ('asin', 'Asin'),
        ('pedas', 'Pedas'),
    ]

    KATEGORI_CHOICES = [
        ('main_course', 'Main Course'),
        ('side_dish', 'Side Dish'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    ]
    
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='menu_images/')
    kategori = models.CharField(max_length=100,null=True, blank=True, choices=KATEGORI_CHOICES)
    tipe_rasa = models.CharField(max_length=100,null=True, blank=True, choices=TIPE_RASA_CHOICES)
    harga = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nama

