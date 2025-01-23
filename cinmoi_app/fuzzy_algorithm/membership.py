def tipe_rasa_membership(tipe_rasa):
    # Fungsi keanggotaan untuk tipe rasa
    if tipe_rasa == 'manis':
        return 0.9
    elif tipe_rasa == 'asin':
        return 0.5
    elif tipe_rasa == 'pedas':
        return 0.8
    return 0
