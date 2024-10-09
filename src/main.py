import pandas as pd


class StatisticMethod:
    datas = {}

    def _init_(self, file_path, sheet_name=0):
        """ 
        Marce
        """
        try:
            data = pd.read_excel(file_path, sheet_name=sheet_name)

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

    def mean(self):
        """ 
        Marce
        """
        pass

    def median(self):
        """ 
        Marce
        """
        pass

    def modus(self):
        """ 
        Marce
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