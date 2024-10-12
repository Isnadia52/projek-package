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
        '''Fungsi untuk menghitung rata-rata dari sekumpulan data.'''
        try:
            data = self.get_data(nama_kolom)
            jumlah_data = sum(data)
            banyaknya_data = len(data)
            nilai_rata_rata = jumlah_data / banyaknya_data if banyaknya_data > 0 else 0
            return nilai_rata_rata
        except:
            print("Kolom atau data tidak valid")

    def median(self, nama_kolom):
        '''Fungsi untuk menentukan nilai tengah dari sekumpulan data.'''
        try:
            data = self.get_data(nama_kolom)
            sorted_data = sorted(data)
            banyaknya_data = len(sorted_data)
            if banyaknya_data % 2 == 1:    # jika banyaknya data berjumlah ganjil
                nilai_median = sorted_data[banyaknya_data // 2]
                return nilai_median
            else:                           # jika banyaknya data berjumlah genap
                nilai_median = (sorted_data[banyaknya_data // 2 - 1] + sorted_data[banyaknya_data // 2]) / 2
                return nilai_median
        except:
            print("Kolom atau data tidak valid")

    def modus(self, nama_kolom):
        '''Fungsi untuk menentukan nilai yang paling sering muncul dari sekumpulan data.'''
        try:
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
        except:
            print("Kolom atau data tidak valid")
            
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