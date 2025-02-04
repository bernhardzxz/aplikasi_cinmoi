# Generated by Django 5.1.4 on 2025-02-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinmoi_app', '0005_remove_menu_harga_alter_menu_kategori_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='harga',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='menu',
            name='kategori',
            field=models.CharField(blank=True, choices=[('appetizer', 'Appetizer'), ('beverage', 'Beverage'), ('congee', 'Congee'), ('dessert', 'Dessert')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='tipe_rasa',
            field=models.CharField(blank=True, choices=[('manis', 'Manis'), ('gurih', 'Gurih'), ('pedas', 'Pedas')], max_length=50, null=True),
        ),
    ]
