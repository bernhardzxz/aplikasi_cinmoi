def get_recommendations(age, preferences, category, price_range):
    # Contoh dataset hidangan
    menu = [
        {"name": "Sup Gurih", "category": "Main Course", "price": 40000, "flavor": ["Gurih"]},
        {"name": "Kue Manis", "category": "Dessert", "price": 30000, "flavor": ["Manis"]},
        {"name": "Dimsum", "category": "Snack", "price": 50000, "flavor": ["Gurih"]},
        {"name": "Rendang Pedas", "category": "Main Course", "price": 75000, "flavor": ["Pedas"]},
    ]

    # Filter berdasarkan usia
    filtered_menu = []
    if age > 40:
        filtered_menu = [item for item in menu if "Gurih" in item["flavor"]]
    else:
        filtered_menu = menu

    # Filter berdasarkan kategori
    filtered_menu = [item for item in filtered_menu if item["category"] == category]

    # Filter berdasarkan harga
    filtered_menu = [item for item in filtered_menu if item["price"] <= price_range]

    # Tambahkan preferensi rasa
    recommended_menus = []
    for item in filtered_menu:
        for flavor in preferences:
            if flavor in item["flavor"] and item not in recommended_menus:
                recommended_menus.append(item["name"])

    return recommended_menus
