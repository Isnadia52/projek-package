# import pandas as pd

# # Mengimpor file Excel
# file_path = 'src\SAMPEL NILAI PROJEK ALGORITMA.xlsx'  # Ganti dengan nama file Excel Anda
# sheet_name = 'Sheet1'  # Ganti dengan nama sheet yang sesuai
# column_name = 'Biologi'  # Ganti dengan nama kolom yang ingin dihitung

# # Membaca data dari file Excel
# data = pd.read_excel(file_path, sheet_name=sheet_name)

# # Menghitung simpangan baku
# simpangan_baku = data[column_name].std()

# print(f'Simpangan Baku dari kolom {column_name}: {simpangan_baku}')

import pandas as pd

def simpanganbaku(file_path, sheet_name, column_name):
    # Membaca data dari file Excel
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Mengambil data dari kolom yang ditentukan dan mengabaikan nilai NaN
    values = data[column_name].dropna()
    
    # Menghitung jumlah dan jumlah data
    n = len(values)
    
    # Menghitung rata-rata
    mean = sum(values) / n
    
    # Menghitung varians
    varians = sum((x - mean) ** 2 for x in values) / n
    
    # Menghitung simpangan baku
    std_dev = varians ** 0.5
    
    return std_dev

# Contoh penggunaan
file_path = 'src/SAMPEL NILAI PROJEK ALGORITMA.xlsx'  # Ganti dengan nama file Excel Anda
sheet_name = 'Sheet1'  # Ganti dengan nama sheet yang sesuai
column_name = 'Biologi'  # Ganti dengan nama kolom yang ingin dihitung

# Menghitung dan mencetak simpangan baku
simpangan_baku = simpanganbaku(file_path, sheet_name, column_name)
print(f'Simpangan Baku dari kolom {column_name}: {simpangan_baku}')
