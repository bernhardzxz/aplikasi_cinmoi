def get_recommendations(age, preferences, category, price_range):
    menu = [
        {"name": "Deep-fried Prawns Rolled / Hekeng", "category": "Appetizer", "price": 68000, "flavor": ["Gurih"]},
        {"name": "Green Tea", "category": "Beverage", "price": 34000, "flavor": ["Manis"]},
        {"name": "Fish Congee with 2 Variant Eggs", "category": "Congee", "price": 42000, "flavor": ["Gurih"]},
        {"name": "Black Forest", "category": "Dessert", "price": 45000, "flavor": ["Manis"]},
    ]

    filtered_menu = []
    if age > 40:
        filtered_menu = [item for item in menu if "Gurih" in item["flavor"]]
    else:
        filtered_menu = menu

    filtered_menu = [item for item in filtered_menu if item["category"] == category]

    filtered_menu = [item for item in filtered_menu if item["price"] <= price_range]

    recommended_menus = []
    for item in filtered_menu:
        for flavor in preferences:
            if flavor in item["flavor"] and item not in recommended_menus:
                recommended_menus.append(item["name"])

    return recommended_menus