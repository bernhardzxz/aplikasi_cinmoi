from django.shortcuts import render, get_object_or_404
from .models import Menu
from django.http import HttpResponse
from .fuzzy_algorithm.recommendation_engine import get_recommendations

def qrcode_view(request):
    return render(request, 'qrcode.html')

def menu_view(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menus})


from django.shortcuts import render, redirect
from django.http import HttpResponse

def recommendation_view(request):
    """
    View untuk menangani form rekomendasi dan menampilkan hasil rekomendasi.
    """
    if request.method == "POST":
        # Ambil data dari form dengan validasi
        name = request.POST.get("name", "").strip()
        age = request.POST.get("age", "").strip()
        preferences = request.POST.get("preferences", "").strip()

        # Validasi input
        if not name or not age or not preferences:
            return HttpResponse("Semua field wajib diisi.", status=400)
        
        try:
            age = int(age)  # Pastikan usia adalah angka
        except ValueError:
            return HttpResponse("Usia harus berupa angka.", status=400)

        # Pisahkan preferensi berdasarkan koma, dan hilangkan spasi ekstra
        preferences_list = [pref.strip() for pref in preferences.split(',') if pref.strip()]

        # Logika algoritma rekomendasi
        recommendations = get_recommendations(age, preferences_list)

        # Kirim data ke template recommendation.html
        return render(request, "recommendation.html", {
            "name": name,
            "recommendations": recommendations,
        })
    # Jika bukan metode POST, arahkan ke halaman utama atau form
    return redirect("menu")  # Ganti "menu" dengan nama URL form Anda

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