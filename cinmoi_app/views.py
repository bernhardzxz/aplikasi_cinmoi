from django.shortcuts import render
from .models import Menu

def qrcode_view(request):
    return render(request, 'qrcode.html')

def menu_view(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menus})