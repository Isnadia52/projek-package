import pandas as pd

def read_data(file_path, sheet_name, column_name):
    """Fungsi untuk membaca data dari Excel dan melakukan analisis."""
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)

        # Analisis berdasarkan kolom
        analisis_kolom(data, column_name)

    except FileNotFoundError:
        print(f'Error: File "{file_path}" tidak ditemukan.')
    except ValueError as ve:
        print(f'Error: {ve}')
    except Exception as e:
        print(f'Terjadi kesalahan: {e}')

def hitung_rata_rata(nilai):
    jumlah_nilai = sum(nilai)
    jumlah_data = len(nilai)
    nilai_rata_rata = jumlah_nilai / jumlah_data if jumlah_data > 0 else 0
    return nilai_rata_rata

def hitung_median(nilai):
    sorted_nilai = sorted(nilai)
    jumlah_data = len(sorted_nilai)
    if jumlah_data % 2 == 1:    # jika jumlah_data ganjil
        nilai_median = sorted_nilai[jumlah_data // 2]
        return nilai_median
    else:                       # jika jumlah_data genap
        nilai_median = (sorted_nilai[jumlah_data // 2 - 1] + sorted_nilai[jumlah_data // 2]) / 2
        return nilai_median
    
def hitung_modus(nilai):
    frekuensi = {}
    for value in nilai:
        if value in frekuensi:
            frekuensi[value] += 1
        else:
            frekuensi[value] = 1
    modus = max(frekuensi, key=frekuensi.get)
    frekuensi_modus = frekuensi[modus]
    return modus, frekuensi_modus

def analisis_kolom(data, column_name):
    if column_name not in data.columns:
        raise ValueError(f'Kolom "{column_name}" tidak ditemukan dalam data.')

    nilai = data[column_name].dropna().astype(float)
    rata_rata = hitung_rata_rata(nilai)
    median = hitung_median(nilai)
    modus, frekuensi_modus = hitung_modus(nilai)

    print(f'\nNilai rata-rata dari kolom {column_name}: {rata_rata}')
    print(f'Nilai median dari kolom {column_name}: {median}')
    print(f'Nilai modus dari kolom {column_name}: {modus}, Frekuensi: {frekuensi_modus}')


file_path = ".\..\SAMPEL NILAI PROJEK ALGORITMA.xlsx"
sheet_name = "Sheet1"           # Ganti dengan nama sheet yang sesuai
column_name = "Fisika"          # Ganti dengan nama kolom yang sesuai
nama_siswa = "Juna"             # Ganti dengan nama siswa yang sesuai

read_data(file_path, sheet_name, column_name, nama_siswa)