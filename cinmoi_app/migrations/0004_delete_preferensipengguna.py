# Generated by Django 5.1.4 on 2025-01-24 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinmoi_app', '0003_menu_harga_menu_kategori_menu_tipe_rasa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PreferensiPengguna',
        ),
    ]
