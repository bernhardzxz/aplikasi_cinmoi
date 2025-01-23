from django import forms

class PreferensiForm(forms.Form):
    TIPE_RASA_CHOICES = [
        ('manis', 'Manis'),
        ('asin', 'Asin'),
        ('pedas', 'Pedas'),
    ]

    KATEGORI_CHOICES = [
        ('main_course', 'Main Course'),
        ('side_dish', 'Side Dish'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    ]

    tipe_rasa = forms.ChoiceField(choices=TIPE_RASA_CHOICES)
    budget = forms.IntegerField(min_value=0)
    kategori_makanan = forms.ChoiceField(choices=KATEGORI_CHOICES)
