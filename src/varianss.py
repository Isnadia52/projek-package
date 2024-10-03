import pandas as pd

def hitung_varians_dari_excel(file_path, kolom):
    try:
        # Membaca data dari file Excel
        data = pd.read_excel(file_path)

        # Mengambil kolom yang diinginkan
        nilai = data[kolom]

        # Menghitung varians
        varians = nilai.var()

        return varians
    except FileNotFoundError:
        return "Error: File tidak ditemukan."
    except KeyError:
        return "Error: Kolom tidak ditemukan."
    except Exception as e:
        return f"Error: {str(e)}"

file_path = '''input file_path dari file yang akan dieksekusi''' 
kolom = '''input sesuai kolom yang akan dihitung''' 

hasil_varians = hitung_varians_dari_excel(file_path, kolom)
print(f"Varians: {hasil_varians}")