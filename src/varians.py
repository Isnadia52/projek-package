def hitung_varians_sampel(data):
    """ Menghitung varians sampel
    Rumus: s² = (1/(n-1)) * Σ(x_i - x̄)² """

    n = len(data) #Menghitung jumlah data
    mean = sum(data) / n #Menghitung rata-rata (mean) data
    varians = sum((x - mean) ** 2 for x in data) / (n - 1) #Ini adalah rumus varians dalam bahasa python #Menghitung varians sampel
    return varians 

def hitung_varians_populasi(data):
    """ Menghitung varians populasi
     Rumus: o² = (1/n) * Σ(x_i - μ)² """

    n = len(data)
    mean = (data) / n
    varians = sum((x - mean) ** 2 for x in data) / n  #Ini adalah rumus varians dalam bahasa python #Menghitung varians populasi
    return varians 

def hitung_varians(data, jenis_varians):
    if jenis_varians == 'sampel':
        return hitung_varians_sampel(data)
    elif jenis_varians == 'populasi':
        return hitung_varians_populasi(data)
    else:
        raise ValueError("Jenis Varians tidak valid. Gunakan 'sampel' atau 'populasi'  ")

def hitung_simpangan_baku(data, jenis_varians):
    "Menghitung simpangan baku dari varians"
    varians = hitung_varians(data, jenis_varians)
    return varians **0.5 #Akar Kuadrat 
