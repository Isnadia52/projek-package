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

    # Menghitung Q1
    if N % 2 == 0:
        Q1 = (data[N // 4 - 1] + data[N // 4]) / 2
        Q2 = (data[N // 2 - 1] + data[N // 2]) / 2
        Q3 = (data[3 * (N // 4) - 1] + data[3 * (N // 4)]) / 2
    else:
        Q1 = data[N // 4]
        Q2 = data[N // 2]
        Q3 = data[3 * (N // 4)]

    return Q1, Q2, Q3
