from django.urls import path
from . import views

urlpatterns = [
    path('', views.qrcode_view, name='qrcode'),  # Halaman utama dengan QRCode
    path('menu/', views.menu_view, name='menu'), # Halaman menu hidangan
]
