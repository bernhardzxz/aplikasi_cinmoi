# def get_recommendations(age, preferences, category, price_range):
#     # Contoh dataset hidangan
#     menu = [
#         {"name": "Deep-fried Prawns Rolled / Hekeng", "category": "Appetizer", "price": 68000, "flavor": ["Gurih"]},
#         {"name": "Green Tea", "category": "Beverage", "price": 34000, "flavor": ["Manis"]},
#         {"name": "Fish Congee with 2 Variant Eggs", "category": "Congee", "price": 42000, "flavor": ["Gurih"]},
#         {"name": "Black Forest", "category": "Dessert", "price": 45000, "flavor": ["Manis"]},
#     ]

#     # Filter berdasarkan usia
#     filtered_menu = []
#     if age > 40:
#         filtered_menu = [item for item in menu if "Gurih" in item["flavor"]]
#     else:
#         filtered_menu = menu

#     # Filter berdasarkan kategori
#     filtered_menu = [item for item in filtered_menu if item["category"] == category]

#     # Filter berdasarkan harga
#     filtered_menu = [item for item in filtered_menu if item["price"] <= price_range]

#     # Tambahkan preferensi rasa
#     recommended_menus = []
#     for item in filtered_menu:
#         for flavor in preferences:
#             if flavor in item["flavor"] and item not in recommended_menus:
#                 recommended_menus.append(item["name"])

#     return recommended_menus

from cinmoi_app.models import Menu  # Import model Menu

def get_recommendations(age, preferences, category, price_range):
    # Ambil semua data menu dari database
    menu = Menu.objects.all()

    # Filter berdasarkan usia (Jika usia > 40, lebih memilih makanan gurih)
    if age > 40:
        menu = menu.filter(tipe_rasa="gurih")

    # Filter berdasarkan kategori
    menu = menu.filter(kategori=category)

    # Filter berdasarkan harga
    menu = menu.filter(harga__lte=price_range)

    # Filter berdasarkan preferensi rasa
    recommended_menus = []
    for item in menu:
        if item.tipe_rasa in preferences:
            recommended_menus.append({
                "name": item.nama,
                "category": item.kategori,
                "price": item.harga,
                "image": item.gambar.url if item.gambar else None,  # Tambahkan gambar
            })

    return recommended_menus
