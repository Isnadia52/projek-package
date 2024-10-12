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

    def varians_sample(self, nama_kolom):
       """Rumus: s² = (1/(n-1)) * Σ(x_i - x̄)²"""
       data = self.get_data(nama_kolom) 
       mean = self.mean(nama_kolom)
       varians = sum((x - mean) ** 2 for x in data) / (len(data) - 1) 
       return varians 
    
    def varians_population(self, nama_kolom):
       """ Rumus: o² = (1/n) * Σ(x_i - μ)² """
       data = self.get_data(nama_kolom)
       mean = self.mean(nama_kolom)
       varians = sum((x - mean) ** 2 for x in data) / len(data)
       return varians 
    
    def varians(self, nama_kolom, jenis_varians):
        if jenis_varians == 'sampel':
            return self.varians_sample(nama_kolom)
        elif jenis_varians == 'populasi':
            return self.varians_population(nama_kolom)
        else:
            raise ValueError("Jenis Varians tidak valid. Gunakan 'sampel' atau 'populasi'  ")
        
    def standard_deviation(self, nama_kolom):
        """Menghitung simpangan baku dari varians"""
        varians = self.varians_sample(nama_kolom)
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

var1 = StatisticMethod("src\\SAMPEL NILAI PROJEK ALGORITMA.xlsx")
print(var1.hitung_varians("Matematika", "sampel"))
