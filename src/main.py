import pandas as pd

class StatisticMethod:
    datas = {}

    def __init__(self, file_path, sheet_name=0):
        """ 
        Marche
        """
        try:
            data = pd.read_excel(file_path, sheet_name=sheet_name)

            kolom = data.columns
            for column in kolom:
                self.datas[column] = data[column].tolist()
            # disini assign data ke variabel datas. datas adalah dictionary,
            # jadi berisi key dan value. key nya adalah nama kolom, valuenya adalah data dari kolom tersebut.
            # Masukkan kodenya di bawah ini

        except FileNotFoundError:
            print(f'Error: File "{file_path}" tidak ditemukan.')
        except ValueError as ve:
            print(f'Error: {ve}')
        except Exception as e:
            print(f'Terjadi kesalahan: {e}')
    
    def get_data(self, nama_kolom):
        return self.datas[nama_kolom]

    def mean(self, column_name):
        '''Fungsi untuk menghitung rata-rata dari sekumpulan angka/nilai.'''
        nilai = self.get_data(column_name)
        jumlah_nilai = sum(nilai)
        banyaknya_nilai = len(nilai)
        nilai_rata_rata = jumlah_nilai / banyaknya_nilai if banyaknya_nilai > 0 else 0
        return nilai_rata_rata

    def median(self):
        """ 
        Marche
        """
        pass

    def modus(self):
        """ 
        Marche
        """
        pass

    def hitung_varians_sampel(self, nama_kolom, data):
       """Rumus: s² = (1/(n-1)) * Σ(x_i - x̄)²"""
       data = self.get_data(nama_kolom)
       n = len(data) 
       mean = sum(data) / n 
       varians = sum((x - mean) ** 2 for x in data) / (n - 1) 
       return varians 
    
    def hitung_varians_populasi(self, nama_kolom, data):
       """ Rumus: o² = (1/n) * Σ(x_i - μ)² """
       data = self.get_data(nama_kolom)
       n = len(data) 
       mean = sum(data) / n 
       varians = sum((x - mean) ** 2 for x in data) / n 
       return varians 
    
    def hitung_varians(self, nama_kolom, jenis_varians):
        if jenis_varians == 'sampel':
            return self.jenis_varians(nama_kolom)
        elif jenis_varians == 'populasi':
            return self.jenis_varians(nama_kolom)
        else:
            raise ValueError("Jenis Varians tidak valid. Gunakan 'sampel' atau 'populasi'  ")
        
    def hitung_simpangan_baku(self, nama_kolom, jenis_varians):
        """Menghitung simpangan baku dari varians"""
        varians = self.hitung_varians(nama_kolom, jenis_varians)
        return varians ** 0.5  # Akar kuadrat
    
    def desil(self):
        """ 
        Daffa
        """
        pass

    def kuartil(self):
        """ 
        Daffa
        """
        pass

    def skewness(self):
        """
        Nadia
        """
        rerata = self.mean()

    def simpangan_rata_rata(self):
        """
        Anugrah
        """
        pass

#var1 = StatisticMethod("SAMPEL NILAI PROJEK ALGORITMA.xlsx")
#print(var1.mean("Matematika"))