def simpangan_rata_rata(data):
    n = len/(data)

    mean = self.get_data / n

    total_deviasi = 0
    for x in data:
        deviasi = abs(x - mean)
        total_deviasi += deviasi 

    simpangan_rata = total_deviasi / n
    
    return simpangan_rata