data = [5, 50, 20, 100, 30, 10, 40]  # data list

def besar(): # mencari nilai terbesar
    global data
    nilai_terbesar = data[0] # 100
    for nilai in data: # 40
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai #100
    return nilai_terbesar

def kecil(): # mencari nilai terkecil
    global data
    nilai_terkecil = data[0]
    for nilai in data:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai
    return nilai_terkecil

# mencetak hasil
print("Data:", data)
print(f"Nilai terbesar: {besar()}")
print(f"Nilai terkecil: {kecil()}",)

