# from django.db import models
# from django.contrib.auth.models import User

# class Menu(models.Model):
#     # Definisikan pilihan untuk tipe rasa
#     TIPE_RASA_CHOICES = [
#         ('manis', 'Manis'),
#         ('gurih', 'Gurih'),
#         ('pedas', 'Pedas'),
#     ]

#     # Definisikan pilihan untuk kategori
#     KATEGORI_CHOICES = [
#         ('appetizer', 'Appetizer'),
#         ('beverage', 'Beverage'),
#         ('congee', 'Congee'),
#         ('dessert', 'Dessert'),
#     ]
    
#     nama = models.CharField(max_length=100)
#     deskripsi = models.TextField()
#     gambar = models.ImageField(upload_to='menu_images/')
#     kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)  # Menggunakan choices untuk kategori
#     tipe_rasa = models.CharField(max_length=50, choices=TIPE_RASA_CHOICES)  # Menggunakan choices untuk tipe rasa
#     class Menu(models.Model):TIPE_RASA_CHOICES = [
#         ('manis', 'Manis'),
#         ('gurih', 'Gurih'),
#         ('pedas', 'Pedas'),
#     ]

#     KATEGORI_CHOICES = [
#         ('appetizer', 'Appetizer'),
#         ('beverage', 'Beverage'),
#         ('congee', 'Congee'),
#         ('dessert', 'Dessert'),
#     ]
    
#     nama = models.CharField(max_length=100)
#     deskripsi = models.TextField()
#     gambar = models.ImageField(upload_to='menu_images/')
#     kategori = models.CharField(max_length=100,null=True, blank=True, choices=KATEGORI_CHOICES)
#     tipe_rasa = models.CharField(max_length=100,null=True, blank=True, choices=TIPE_RASA_CHOICES)

#     def __str__(self):
#         return self.nama


from django.db import models

class Menu(models.Model):
    # Definisikan pilihan untuk tipe rasa
    TIPE_RASA_CHOICES = [
        ('manis', 'Manis'),
        ('gurih', 'Gurih'),
        ('pedas', 'Pedas'),
    ]

    # Definisikan pilihan untuk kategori
    KATEGORI_CHOICES = [
        ('appetizer', 'Appetizer'),
        ('beverage', 'Beverage'),
        ('congee', 'Congee'),
        ('dessert', 'Dessert'),
    ]
    
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='menu_images/')
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)  # Menggunakan choices untuk kategori
    tipe_rasa = models.CharField(max_length=50, choices=TIPE_RASA_CHOICES)  # Menggunakan choices untuk tipe rasa
    harga = models.DecimalField(max_digits=10, decimal_places=2)  # Menambahkan field harga

    def __str__(self):
        return self.nama
