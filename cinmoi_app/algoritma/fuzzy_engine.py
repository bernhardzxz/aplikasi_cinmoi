# import numpy as np
# import skfuzzy as fuzz
# import skfuzzy.control as ctrl

# # Dataset hidangan
# menu = [
#     {"name": "Deep-fried Prawns Rolled / Hekeng", "category": "Appetizer", "price": 68000, "flavor": ["Gurih"]},
#     {"name": "Green Tea", "category": "Beverage", "price": 34000, "flavor": ["Manis"]},
#     {"name": "Fish Congee with 2 Variant Eggs", "category": "Congee", "price": 42000, "flavor": ["Gurih"]},
#     {"name": "Black Forest", "category": "Dessert", "price": 45000, "flavor": ["Manis"]},
# ]

# def fuzzy_sugeno_recommendation(age, price_range, preferences, category):
#     # Definisi variabel fuzzy
#     age_var = ctrl.Antecedent(np.arange(18, 61, 1), 'age')
#     price_var = ctrl.Antecedent(np.arange(20000, 100000, 1000), 'price')
#     recommendation = ctrl.Consequent(np.arange(0, 101, 1), 'recommendation', defuzzify_method='wtaver')

#     # Membership functions untuk umur
#     age_var['young'] = fuzz.trimf(age_var.universe, [18, 25, 30])
#     age_var['adult'] = fuzz.trimf(age_var.universe, [26, 40, 50])
#     age_var['old'] = fuzz.trimf(age_var.universe, [41, 60, 60])

#     # Membership functions untuk harga
#     price_var['cheap'] = fuzz.trimf(price_var.universe, [20000, 30000, 40000])
#     price_var['medium'] = fuzz.trimf(price_var.universe, [40000, 60000, 80000])
#     price_var['expensive'] = fuzz.trimf(price_var.universe, [60000, 80000, 100000])

#     # Output berupa nilai rekomendasi tetap (Sugeno)
#     recommendation['low'] = 40
#     recommendation['medium'] = 60
#     recommendation['high'] = 85

#     # Definisi aturan fuzzy
#     rule1 = ctrl.Rule(age_var['young'] & price_var['cheap'], recommendation['high'])
#     rule2 = ctrl.Rule(age_var['old'] & price_var['expensive'], recommendation['low'])
#     rule3 = ctrl.Rule(age_var['old'] & price_var['medium'], recommendation['medium'])

#     # Sistem kontrol fuzzy
#     recommendation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
#     recommendation_sim = ctrl.ControlSystemSimulation(recommendation_ctrl)

#     # Input nilai dari user
#     recommendation_sim.input['age'] = age
#     recommendation_sim.input['price'] = price_range

#     # Hitung hasil rekomendasi
#     recommendation_sim.compute()
#     recommendation_score = recommendation_sim.output['recommendation']

#     # Filter menu berdasarkan aturan fuzzy
#     filtered_menu = [item for item in menu if item["category"] == category and item["price"] <= price_range]

#     # Tambahkan preferensi rasa
#     recommended_menus = []
#     for item in filtered_menu:
#         for flavor in preferences:
#             if flavor in item["flavor"] and item not in recommended_menus:
#                 recommended_menus.append(item["name"])

#     return recommended_menus, recommendation_score
