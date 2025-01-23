from django.shortcuts import render
from .models import Menu

def qrcode_view(request):
    # Menampilkan halaman utama dengan QRCode
    return render(request, 'qrcode.html')

def menu_view(request):
    # Menampilkan halaman menu hidangan
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menus': menus})
