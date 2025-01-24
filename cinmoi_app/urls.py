from django.urls import path
from . import views

urlpatterns = [
    path('', views.qrcode_view, name='qrcode'),
    path('menu/', views.menu_view, name='menu'),
    path('recommendation/', views.recommendation_view, name='recommendation'),
]
