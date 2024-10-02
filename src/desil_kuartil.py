import pandas as pd

def hitung_desil(data, desil_ke):
    """
    Menghitung nilai desil untuk data yang diberikan.
    
    Parameters:
        data (list atau Pandas Series): Data input yang akan dihitung desilnya.
        desil_ke (int): Nilai desil ke berapa yang akan dihitung (1-9).
    
    Returns:
        float: Nilai desil yang sesuai.
    """
    if desil_ke < 1 or desil_ke > 9:
        raise ValueError("Desil ke harus antara 1 dan 9")
    
    # Menggunakan pandas untuk menghitung desil
    data_series = pd.Series(data)
    desil_value = data_series.quantile(desil_ke / 10)
    return desil_value

def hitung_kuartil(data, kuartil_ke):
    """
    Menghitung nilai kuartil untuk data yang diberikan.
    
    Parameters:
        data (list atau Pandas Series): Data input yang akan dihitung kuartilnya.
        kuartil_ke (int): Nilai kuartil ke berapa yang akan dihitung (1-3).
    
    Returns:
        float: Nilai kuartil yang sesuai.
    """
    if kuartil_ke < 1 or kuartil_ke > 3:
        raise ValueError("Kuartil ke harus antara 1 dan 3")
    
    # Menggunakan pandas untuk menghitung kuartil
    data_series = pd.Series(data)
    kuartil_value = data_series.quantile(kuartil_ke / 4)
    return kuartil_value
