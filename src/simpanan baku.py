# import math

# def simpangan_baku(data):
#     mean = sum(data) / len(data)
#     variance = sum((x - mean) ** 2 for x in data) / len(data)
#     simpangan_baku = math.sqrt(variance)
#     return simpangan_baku
import math

def simpanan_baku(data):
    # Menghitung rata-rata (mean)
    mean = sum(data) / len(data)
    
    # Menghitung varians
    varians = sum((x - mean) ** 2 for x in data) / len(data)
    
    # Menghitung simpanan baku
    std_dev = math.sqrt(varians)
    
    return std_dev
