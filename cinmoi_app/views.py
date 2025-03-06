from django.shortcuts import render
from .models import Menu
from django.http import HttpResponse
from .algoritma.recommendation_engine import get_recommendations


def recommendation_view(request):
    if request.method == "POST":
        
        name = request.POST.get("name", "").strip()
        age = request.POST.get("age", "").strip()
        preferences = request.POST.get("preferences", "").split(',')
        category = request.POST.get("category", "").strip()
        price_range = request.POST.get("price_range", "").strip()

      
        if not name or not age or not preferences or not category or not price_range:
            return HttpResponse("Form tidak lengkap. Harap isi semua bidang.", status=400)

        try:
            age = int(age)
            price_range = int(price_range)
        except ValueError:
            return HttpResponse("Usia dan harga harus berupa angka yang valid.", status=400)

        
        recommendations = get_recommendations(age, preferences, category, price_range)


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


        context = {
            'nama': nama,
            'usia': usia,
            'kategori': kategori,
            'rasa': rasa,
        }
        return render(request, 'recommendation.html', context)
    return render(request, 'menu.html')

# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Menu
# from .algoritma.fuzzy_engine import fuzzy_sugeno_recommendation  # Menggunakan Fuzzy Sugeno

# def menu_view(request):
#     menus = Menu.objects.all()
#     return render(request, 'menu.html', {'menu': menus})

# def recommendation_view(request):
#     if request.method == "POST":
#         # Debugging: Cetak data yang diterima dari form
#         print("Form Data:", request.POST)

#         # Ambil data dari form
#         name = request.POST.get("name", "").strip()
#         age = request.POST.get("age", "").strip()
#         category = request.POST.get("category", "").strip()
#         price_range = request.POST.get("price_range", "").strip()
#         preferences = request.POST.getlist("preferences")  # Ambil multiple select dengan list

#         # Debugging: Cetak hasil parsing input
#         print(f"Nama: {name}, Usia: {age}, Kategori: {category}, Harga: {price_range}, Preferensi: {preferences}")

#         # Validasi input
#         if not name or not age or not category or not price_range or not preferences:
#             return HttpResponse("Form tidak lengkap. Harap isi semua bidang.", status=400)

#         try:
#             age = int(age)
#             price_range = int(price_range)
#         except ValueError:
#             return HttpResponse("Usia dan harga harus berupa angka yang valid.", status=400)

#         # Gunakan algoritma Fuzzy Sugeno
#         recommendations, recommendation_score = fuzzy_sugeno_recommendation(age, price_range, preferences, category)

#         # Ambil data menu dari database berdasarkan hasil rekomendasi
#         recommended_menus = Menu.objects.filter(nama__in=recommendations)

#         # Kirim data ke template
#         return render(request, "recommendation.html", {
#             "name": name,
#             "recommendations": recommended_menus,
#             "recommendation_score": recommendation_score,
#         })

#     return HttpResponse("Permintaan tidak valid. Harap gunakan formulir untuk mengirim data.", status=400)

# def qrcode_view(request):
#     return render(request, 'qrcode.html')