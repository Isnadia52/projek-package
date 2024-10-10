import pandas as pd

def hitung_skewness_kurtosis(data, kolom):
    # Menghitung statistik dasar
    n = len(data[kolom])
    mean = data[kolom].mean()
    std_dev = data[kolom].std()

    # Menghitung skewness
    skewness = (1/n) * sum(((data[kolom] - mean) / std_dev) ** 3)

    # Menghitung kurtosis
    kurtosis = (1/n) * sum(((data[kolom] - mean) / std_dev) ** 4) - 3

    return skewness, kurtosis

# Membaca data dari file excel
file_path = 'src\SAMPEL NILAI PROJEK ALGORITMA.xlsx'  # Ganti dengan path ke file Anda
data = pd.read_excel(file_path)

# Ganti 'nama_kolom' dengan nama kolom yang ingin dianalisis
kolom_anda = 'Biologi'  # Ganti dengan nama kolom yang sesuai

skewness, kurtosis = hitung_skewness_kurtosis(data, kolom_anda)

print(f'Skewness dari {kolom_anda}: {skewness}')
print(f'Kurtosis dari {kolom_anda}: {kurtosis}')