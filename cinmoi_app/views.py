import qrcode
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from .forms import PreferensiForm

def rekomendasi_view(request):
    rekomendasi = None
    if request.method == 'POST':
        form = PreferensiForm(request.POST)
        if form.is_valid():
            tipe_rasa = form.cleaned_data['tipe_rasa']
            budget = form.cleaned_data['budget']
            kategori = form.cleaned_data['kategori_makanan']

            # Filter menu berdasarkan preferensi
            rekomendasi = Menu.objects.filter(
                tipe_rasa=tipe_rasa,
                kategori=kategori,
                harga__lte=budget
            )

            # Generate QR Code
            qr_data = f"http://127.0.0.1:8000/rekomendasi/?tipe_rasa={tipe_rasa}&budget={budget}&kategori={kategori}"
            qr_code = qrcode.make(qr_data)
            qr_image = BytesIO()
            qr_code.save(qr_image)
            qr_image.seek(0)

            return render(request, 'rekomendasi.html', {
                'form': form,
                'rekomendasi': rekomendasi,
                'qr_image': qr_image
            })
    else:
        form = PreferensiForm()

    return render(request, 'rekomendasi.html', {'form': form, 'rekomendasi': rekomendasi})


def qrcode_view(request):
    return render(request, 'qrcode.html')

def menu_view(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menus})