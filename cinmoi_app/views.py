from django.shortcuts import render
from .models import Menu
from django.http import HttpResponse
from .fuzzy_algorithm.recommendation_engine import get_recommendations


def recommendation_view(request):
    if request.method == "POST":
        # Ambil data dari form
        name = request.POST.get("name", "").strip()
        age = request.POST.get("age", "").strip()
        preferences = request.POST.get("preferences", "").split(',')
        category = request.POST.get("category", "").strip()
        price_range = request.POST.get("price_range", "").strip()

        # Validasi input
        if not name or not age or not preferences or not category or not price_range:
            return HttpResponse("Form tidak lengkap. Harap isi semua bidang.", status=400)

        try:
            age = int(age)
            price_range = int(price_range)
        except ValueError:
            return HttpResponse("Usia dan harga harus berupa angka yang valid.", status=400)

        # Dapatkan rekomendasi
        recommendations = get_recommendations(age, preferences, category, price_range)

        # Kirim data ke template
        return render(request, "recommendation.html", {
            "name": name,
            "recommendations": recommendations,
        })

    return HttpResponse("Permintaan tidak valid. Harap gunakan formulir untuk mengirim data.", status=400)

def qrcode_view(request):
    return render(request, 'qrcode.html')

def menu_view(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menus})

def recommendation(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        usia = request.POST.get('usia')
        kategori = request.POST.get('kategori')
        rasa = request.POST.get('rasa')

        # Lakukan logika rekomendasi di sini
        context = {
            'nama': nama,
            'usia': usia,
            'kategori': kategori,
            'rasa': rasa,
        }
        return render(request, 'recommendation.html', context)
    return render(request, 'menu.html')