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
            # jadi berisi key dan value. key nya adalah nama kolom, value nya
            # adalah data dari kolom tersebut.
            # Masukkan kodenya di bawah ini

        except FileNotFoundError:
            print(f'Error: File "{file_path}" tidak ditemukan.')
        except ValueError as ve:
            print(f'Error: {ve}')
        except Exception as e:
            print(f'Terjadi kesalahan: {e}')
    

    def get_data(self, nama_kolom):
        return self.datas[nama_kolom]

    def mean(self):
        """ 
        Marche
        """
        pass

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

    def simpangan_rata_rata(self):
        """
        Anugrah
        """
        pass