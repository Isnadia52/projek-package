
def hitung_desil(data, k):
    N = len(data)
    '''Rumus untuk menghitung posisi desil ke-k:
    P = k * (N + 1) / 10 '''
    posisi = k * (N + 1) / 10
    
    posisi_bawah = int(posisi) - 1
    posisi_atas = posisi_bawah + 1 
    
    # Jika posisi tepat pada data, kembalikan nilainya
    if posisi.is_integer():
        return data[posisi_bawah]

    if posisi_atas < N: 
        nilai_bawah = data[posisi_bawah]
        nilai_atas = data[posisi_atas]
        interpolasi = nilai_bawah + (posisi - (posisi_bawah + 1)) * (nilai_atas - nilai_bawah)
        return interpolasi
    else:
        return data[posisi_bawah] 

def hitung_kuartil(data):
    data.sort()
    N = len(data)
    
    # Fungsi untuk menghitung median
    def median(data):
        N = len(data)
        mid = N // 2
        if N % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]

    Q2 = median(data)  # Kuartil 2 (Median)
    
    # Q1 dan Q3
    if N % 2 == 0:
        Q1 = median(data[:N // 2])  # Pertengahan data bawah
        Q3 = median(data[N // 2:])  # Pertengahan data atas
    else:
        Q1 = median(data[:N // 2])  # Pertengahan data bawah
        Q3 = median(data[N // 2 + 1:])  # Pertengahan data atas
    
    return Q1, Q2, Q3