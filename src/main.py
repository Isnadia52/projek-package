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

    def variansi(self):
        """ 
        Naca
        """
        pass

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

    def simpangan_baku(self):
        """
        Kiyah
        """

    def skewness(self):
        """
        Nadia
        """
        rerata = self.mean()

    def simpangan_rata_rata(self, column_name):
        rata_rata = self.mean(column_name)
        nilai = self.get_data(column_name)
        n = len(nilai)
        total_deviasi = 0
        for x in nilai:
            deviasi = abs(x - rata_rata)
            total_deviasi += deviasi 

        simpangan_rata = total_deviasi / n
        
        return simpangan_rata
       

var1 = StatisticMethod("D:\projek-package\src\SAMPEL NILAI PROJEK ALGORITMA.xlsx")
print(var1.simpangan_rata_rata("Matematika"))