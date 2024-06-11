def sifrele():

    giris_metni = input("Lütfen Metni Giriniz: ")
    anahtar = int(input("Lütfen anahtar değer giriniz: "))
    metin = giris_metni.replace(" ","").lower()

    # satır sayısı = anahtar
    # sütun sayısı = metin uzunluğu 

    # satır sayısını anahtar değerinde, sütun sayısını metnin uzunluğundan alır 
    rail = [['' for _ in range(len(metin))] for _ in range(anahtar)]
    
    row, direction = 0, 1  
    for i, char in enumerate(metin):
        rail[row][i] = char  
        if row == 0:
            direction = 1  # Aşağı in 
        elif row == anahtar - 1:
            direction = -1  # Yukarı çık 
        row += direction

    
    sifreli_metin = ''.join(''.join(r) for r in rail)
    print(f"Şifreli Metin: {sifreli_metin}")

def coz():

    giris_metni = input("Lütfen Metni Giriniz: ")
    anahtar = int(input("Lütfen anahtar değer giriniz: "))
    metin = giris_metni.replace(" ","").lower()
    
    n = len(metin)
    rail_pattern = ['' for _ in range(n)]
    row, direction = 0, 1
    for i in range(n):
        rail_pattern[i] = row
        if row == 0:
            direction = 1 
        elif row == anahtar - 1:
            direction = -1  
        row += direction

    
    rail = [['' for _ in range(n)] for _ in range(anahtar)]
    index = 0
    for r in range(anahtar):
        for i in range(n):
            if rail_pattern[i] == r:
                rail[r][i] = metin[index]
                index += 1

    
    cozulmus_metin = ''
    row, direction = 0, 1
    for i in range(n):
        cozulmus_metin += rail[row][i]
        if row == 0:
            direction = 1  
        elif row == anahtar - 1:
            direction = -1 
        row += direction

    print(f"Şifreli Metin: {cozulmus_metin}") 


sifrele()
coz()