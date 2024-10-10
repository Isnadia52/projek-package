import pandas as pd

def read_data(file_path, sheet_name, column_name):
    '''Fungsi untuk membaca data dari Excel dan melakukan analisis berdasakan kolom'''
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)

        analisis_kolom(data, column_name)

    except FileNotFoundError:
        print(f'Error: File "{file_path}" tidak ditemukan.')
    except ValueError as ve:
        print(f'Error: {ve}')
    except Exception as e:
        print(f'Terjadi kesalahan: {e}')

def mean(nilai):
    '''Fungsi untuk menghitung rata-rata dari sekumpulan angka/nilai.'''
    jumlah_nilai = sum(nilai)
    banyaknya_nilai = len(nilai)
    nilai_rata_rata = jumlah_nilai / banyaknya_nilai if banyaknya_nilai > 0 else 0
    return nilai_rata_rata

def median(nilai):
    '''Fungsi untuk menentukan median dari sekumpulan nilai.'''
    sorted_nilai = sorted(nilai)
    banyaknya_nilai = len(sorted_nilai)
    if banyaknya_nilai % 2 == 1:    # jika banyaknya nilai berjumlah ganjil
        nilai_median = sorted_nilai[banyaknya_nilai // 2]
        return nilai_median
    else:                           # jika banyaknya nilai berjumlah genap
        nilai_median = (sorted_nilai[banyaknya_nilai // 2 - 1] + sorted_nilai[banyaknya_nilai // 2]) / 2
        return nilai_median
    
def modus(nilai):
    '''Fungsi untuk menentukan nilai modus dari sekumpulan nilai.'''
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
    '''Melakukan analisis statistik pada kolom tertentu dari DataFrame.'''
    if column_name not in data.columns:
        raise ValueError(f'Kolom "{column_name}" tidak ditemukan dalam data.')

    nilai = data[column_name].dropna().astype(float)
    rata_rata = mean(nilai)
    nilai_median = median(nilai)
    nilai_modus, frekuensi_modus = modus(nilai)

    print(f'\nNilai rata-rata dari kolom {column_name}: {rata_rata}')
    print(f'Nilai median dari kolom {column_name}: {nilai_median}')
    print(f'Nilai modus dari kolom {column_name}: {nilai_modus}, Frekuensi: {frekuensi_modus}')


file_path = "D:\projek-package\src\SAMPEL NILAI PROJEK ALGORITMA.xlsx" #Ganti dengan file path file yang ingin dihitung statistiknya
sheet_name = "Sheet1"           # Ganti dengan nama sheet yang sesuai
column_name = "Fisika"          # Ganti dengan nama kolom yang sesuai

read_data(file_path, sheet_name, column_name)