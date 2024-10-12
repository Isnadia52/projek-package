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
        try: 
             if jenis_varians == 'sampel':
                return self.varians_sample(nama_kolom)
             elif jenis_varians == 'populasi':
                return self.varians_population(nama_kolom)
             else:
               raise ValueError("Jenis Varians tidak valid. Gunakan 'sampel' atau 'populasi'  ")
        except:
            print('Kolom atau data tidak valid! ')
             
        
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

    def skewness(self, nama_kolom):
        try:
            n = len(self.get_data(nama_kolom))
            mean = self.mean(nama_kolom)
            std_dev = self.standard_deviation(nama_kolom)

            # Menghitung skewness
            skewness = (1/n) * sum(((self[nama_kolom] - mean) / std_dev) ** 3)
            return skewness
        except:
            print("Kolom atau data tidak valid!")

    def mean_deviation(self, nama_kolom):
        try:
            rata_rata = self.mean(nama_kolom)
            nilai = self.get_data(nama_kolom)
            n = len(nilai)
            total_deviasi = 0
            for x in nilai:
                deviasi = abs(x - rata_rata)
                total_deviasi += deviasi 

            simpangan_rata = round(total_deviasi / n, 2)
            
            return simpangan_rata
        except:
            print("kolom atau data tidak valid")