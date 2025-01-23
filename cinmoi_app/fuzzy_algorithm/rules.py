def apply_rules(tipe_rasa, harga, kategori):
    # Aturan fuzzy berdasarkan preferensi
    if tipe_rasa == 'manis' and kategori == 'dessert':
        return 0.8 * harga  # Harga lebih rendah untuk dessert manis
    elif tipe_rasa == 'asin' and kategori == 'main_course':
        return 1.0 * harga  # Harga standar untuk main course asin
    return 0.5 * harga
