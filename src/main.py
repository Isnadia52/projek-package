import pandas as pd

class StatisticMethod:
    datas = {}

    def __init__(self, file_path, sheet_name=0):
        try:
            data = pd.read_excel(file_path, sheet_name=sheet_name)

            kolom = data.columns
            for column in kolom:
                self.datas[column] = data[column].tolist()
            # disini assign data ke variabel datas. datas adalah dictionary,
            # jadi berisi key dan value. key nya adalah nama kolom, valuenya adalah data dari kolom tersebut.

        except FileNotFoundError:
            print(f'Error: File "{file_path}" tidak ditemukan.')
        except ValueError as ve:
            print(f'Error: {ve}')
        except Exception as e:
            print(f'Terjadi kesalahan: {e}')
    
    def get_data(self, nama_kolom):
        return self.datas[nama_kolom]

    def mean(self, nama_kolom):
        '''Fungsi untuk menghitung rata-rata dari sekumpulan angka/nilai.'''
        nilai = self.get_data(nama_kolom)
        jumlah_nilai = sum(nilai)
        banyaknya_nilai = len(nilai)
        nilai_rata_rata = jumlah_nilai / banyaknya_nilai if banyaknya_nilai > 0 else 0
        return nilai_rata_rata

    def median(self, nama_kolom):
        '''Fungsi untuk menentukan median dari sekumpulan nilai.'''
        nilai = self.get_data(nama_kolom)
        sorted_nilai = sorted(nilai)
        banyaknya_nilai = len(sorted_nilai)
        if banyaknya_nilai % 2 == 1:    # jika banyaknya nilai berjumlah ganjil
            nilai_median = sorted_nilai[banyaknya_nilai // 2]
            return nilai_median
        else:                           # jika banyaknya nilai berjumlah genap
            nilai_median = (sorted_nilai[banyaknya_nilai // 2 - 1] + sorted_nilai[banyaknya_nilai // 2]) / 2
            return nilai_median

    def modus(self, nama_kolom):
        '''Fungsi untuk menentukan nilai modus dari sekumpulan nilai.'''
        nilai = self.get_data(nama_kolom)
        frekuensi = {}
        for value in nilai:
            if value in frekuensi:
                frekuensi[value] += 1
            else:
                frekuensi[value] = 1
        modus = max(frekuensi, key=frekuensi.get)
        frekuensi_modus = frekuensi[modus]
        return modus, frekuensi_modus

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

    def simpangan_rata_rata(self):
        """
        Anugrah
        """
        pass

var1 = StatisticMethod("SAMPEL NILAI PROJEK ALGORITMA.xlsx")
print(var1.mean("Fisika"))