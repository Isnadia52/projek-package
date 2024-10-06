def hitung_mean(data):
    """Menghitung rata-rata dari sekumpulan data."""
    return sum(data) / len(data) if data else 0

def hitung_simpangan_rata_rata(data):
    """Menghitung simpangan rata-rata dari sekumpulan data."""
    if not data:
        return 0
    mean = hitung_mean(data)
    selisih_abs = [abs(x - mean) for x in data]
    simpangan_rata_rata = hitung_mean(selisih_abs)
    return simpangan_rata_rata
