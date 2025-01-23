from .membership import tipe_rasa_membership
from .rules import apply_rules
from .defuzzification import defuzzify

def get_recommendation(tipe_rasa, harga, kategori):
    # Menggunakan algoritma Fuzzy Sugeno untuk memberikan rekomendasi
    membership_value = tipe_rasa_membership(tipe_rasa)
    rule_output = apply_rules(tipe_rasa, harga, kategori)
    final_score = defuzzify(rule_output)

    return final_score
