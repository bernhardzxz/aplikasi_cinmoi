# import skfuzzy.membership as fuzz
# from skfuzzy import control as ctrl
# import numpy as np

# def fuzzy_sugeno(age, price):
#     # Define fuzzy variables
#     usia = ctrl.Antecedent(np.arange(0, 101, 1), 'usia')
#     harga = ctrl.Antecedent(np.arange(0, 100001, 1000), 'harga')
#     rekomendasi = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'rekomendasi')

#     # Membership functions for 'usia'
#     usia['muda'] = fuzz.trapmf(usia.universe, [0, 0, 18, 30])
#     usia['dewasa'] = fuzz.trapmf(usia.universe, [20, 40, 60, 80])
#     usia['tua'] = fuzz.trapmf(usia.universe, [60, 80, 100, 100])

#     # Membership functions for 'harga'
#     harga['murah'] = fuzz.trapmf(harga.universe, [0, 0, 30000, 60000])
#     harga['sedang'] = fuzz.trimf(harga.universe, [40000, 70000, 100000])
#     harga['mahal'] = fuzz.trapmf(harga.universe, [80000, 100000, 100000, 100000])

#     # Membership functions for 'rekomendasi'
#     rekomendasi['rendah'] = fuzz.trimf(rekomendasi.universe, [0, 0, 0.5])
#     rekomendasi['sedang'] = fuzz.trimf(rekomendasi.universe, [0.25, 0.5, 0.75])
#     rekomendasi['tinggi'] = fuzz.trimf(rekomendasi.universe, [0.5, 1, 1])

#     # Define rules
#     rule1 = ctrl.Rule(usia['muda'] & harga['murah'], rekomendasi['tinggi'])
#     rule2 = ctrl.Rule(usia['dewasa'] & harga['sedang'], rekomendasi['sedang'])
#     rule3 = ctrl.Rule(usia['tua'] & harga['mahal'], rekomendasi['rendah'])

#     # Create control system
#     recommendation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
#     recommendation = ctrl.ControlSystemSimulation(recommendation_ctrl)

#     # Input fuzzy values
#     recommendation.input['usia'] = age
#     recommendation.input['harga'] = price

#     # Compute result
#     recommendation.compute()
#     return recommendation.output['rekomendasi']


# def get_recommendations(age, preferences, category, price_range):
#     from models import Menu  # Import model Menu
    
#     # Filter menus sesuai dengan input pengguna
#     menus = Menu.objects.filter(
#         tipe_rasa__icontains=preferences, 
#         kategori=category, 
#         harga__lte=price_range
#     )

#     # Evaluasi dengan Fuzzy Sugeno
#     recommendations = []
#     for menu in menus:
#         score = fuzzy_sugeno(age, menu.harga)
#         if score > 0.5:  # Ambang batas rekomendasi
#             recommendations.append(menu)

#     return recommendations
