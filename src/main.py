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

    def desil(self, nama_kolom):
        data = self.get_data(nama_kolom)
        N = len(data)
        '''Rumus untuk menghitung posisi desil ke-k:
        P = k * (N + 1) / 10 '''
        posisi = k * (N + 1) / 10
        
        posisi_bawah = int(posisi) - 1
        posisi_atas = posisi_bawah + 1 
        
        # Jika posisi tepat pada data, kembalikan nilainya
        if posisi.is_integer():
            return data[posisi_bawah]

        if posisi_atas < N: 
            nilai_bawah = data[posisi_bawah]
            nilai_atas = data[posisi_atas]
            interpolasi = nilai_bawah + (posisi - (posisi_bawah + 1)) * (nilai_atas - nilai_bawah)
            return interpolasi
        else:
            return data[posisi_bawah] 
        

    def kuartil(self, nama_kolom):
        data = self.get_data(nama_kolom)
        data.sort()
        N = len(data)

        # Menghitung kuartil
        if N % 2 == 0:
            Q1 = (data[N // 4 - 1] + data[N // 4]) / 2
            Q2 = (data[N // 2 - 1] + data[N // 2]) / 2
            Q3 = (data[3 * (N // 4) - 1] + data[3 * (N // 4)]) / 2
        else:
            Q1 = data[N // 4]
            Q2 = data[N // 2]
            Q3 = data[3 * (N // 4)]

        return Q1, Q2, Q3

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

#var1 = StatisticMethod("SAMPEL NILAI PROJEK ALGORITMA.xlsx")
#print(var1.desil("Matematika"))