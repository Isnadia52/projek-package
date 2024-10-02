import pandas as pd

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

    '''print hasil analisis berdasarkan kolom
    print rata-rata, median, modus, dan frekuensi modus'''

def analisis_nama_siswa(data, nama_siswa):
    if 'Nama Siswa' not in data.columns:
        raise ValueError('Kolom "Nama Siswa" tidak ditemukan dalam data.')
    
    data_siswa = data[data['Nama Siswa'] == nama_siswa]
    if data_siswa.empty:
        raise ValueError(f'Siswa atas nama {nama_siswa} tidak ditemukan dalam data.')

    nilai_siswa = data_siswa.iloc[0, 1:].dropna().astype(float).tolist()  #mengambil semua nilai kecuali nama siswa
    rata_rata = hitung_rata_rata(nilai_siswa)
    median = hitung_median(nilai_siswa)
    modus, frekuensi_modus = hitung_modus(nilai_siswa)

    '''print hasil berdasarkan analisis nama siswa
    print rata-rata, median, modus, dan frekuensi modus'''

'''input variabel file path, sheet name, column name, dan nama siswa(jika ingin menghitung nilai siswa)'''
file_path = '''input file_path dari file yang akan dieksekusi'''
sheet_name = '''input sheet yang akan dihitung'''
column_name = '''input sesuai kolom yang akan dihitung'''
nama_siswa = '''input sesuai nama siswa'''

try:
    data = pd.read_excel(file_path, sheet_name=sheet_name)

    '''Analisis berdasarkan kolom'''
    analisis_kolom(data, column_name)

    '''Analisis berdasarkan nama siswa'''
    analisis_nama_siswa(data, nama_siswa)

except FileNotFoundError:
    print(f'Error: File "{file_path}" tidak ditemukan.')
except ValueError as ve:
    print(f'Error: {ve}')
except Exception as e:
    print(f'Terjadi kesalahan: {e}')