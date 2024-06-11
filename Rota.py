def sifrele():

    giris_metni = input("Lütfen Metni Giriniz: ")
    anahtar = int(input("Lütfen anahtar değer giriniz: "))
    metin = giris_metni.replace(" ","").lower()

    if len(metin) > anahtar * anahtar:
        raise ValueError("Metin, matris boyutundan büyük olamaz")

    # Metni matrise yerleştir
    metin += 'a' * (anahtar * anahtar - len(metin)) 
    matrix = [['' for _ in range(anahtar)] for _ in range(anahtar)]
    for i, char in enumerate(metin):
        row = i // anahtar
        col = i % anahtar
        matrix[row][col] = char

    # Şifrelenmiş metni sol alt köşeden başlayarak saat yönünde spiral şekilde oluştur
    sifreli_metin = ''
    direction = 0  # 0: yukarı, 1: sağa, 2: aşağı, 3: sola
    row, col = anahtar - 1, 0
    visited = [[False] * anahtar for _ in range(anahtar)]

    while not visited[row][col]:
        sifreli_metin += matrix[row][col]
        visited[row][col] = True

        if direction == 0:  # yukarı git
            if row > 0 and not visited[row - 1][col]:
                row -= 1
            else:
                direction = 1
                col += 1
        elif direction == 1:  # sağa git
            if col < anahtar - 1 and not visited[row][col + 1]:
                col += 1
            else:
                direction = 2
                row += 1
        elif direction == 2:  # aşağı git
            if row < anahtar - 1 and not visited[row + 1][col]:
                row += 1
            else:
                direction = 3
                col -= 1
        elif direction == 3:  # sola git
            if col > 0 and not visited[row][col - 1]:
                col -= 1
            else:
                direction = 0
                row -= 1

    print(f"Şifreli Metin: {sifreli_metin}") 



def coz():

    giris_metni = input("Lütfen Metni Giriniz: ")
    anahtar = int(input("Lütfen anahtar değer giriniz: "))
    metin = giris_metni.replace(" ","").lower()

    if len(metin) != anahtar * anahtar:
        raise ValueError("Şifreli metin, matris boyutu ile eşleşmiyor")

    # Şifreli metni matrise yerleştir
    matrix = [['' for _ in range(anahtar)] for _ in range(anahtar)]
    direction = 0  # 0: yukarı, 1: sağa, 2: aşağı, 3: sola
    row, col = anahtar - 1, 0
    visited = [[False] * anahtar for _ in range(anahtar)]
    sifrelenmis_index = 0

    while sifrelenmis_index < len(metin):
        matrix[row][col] = metin[sifrelenmis_index]
        visited[row][col] = True
        sifrelenmis_index += 1

        if direction == 0:  # yukarı git
            if row > 0 and not visited[row - 1][col]:
                row -= 1
            else:
                direction = 1
                col += 1
        elif direction == 1:  # sağa git
            if col < anahtar - 1 and not visited[row][col + 1]:
                col += 1
            else:
                direction = 2
                row += 1
        elif direction == 2:  # aşağı git
            if row < anahtar - 1 and not visited[row + 1][col]:
                row += 1
            else:
                direction = 3
                col -= 1
        elif direction == 3:  # sola git
            if col > 0 and not visited[row][col - 1]:
                col -= 1
            else:
                direction = 0
                row -= 1

    # Orijinal metni matristen oku
    cozulmus_metin = ''
    for i in range(anahtar):
        for j in range(anahtar):
            cozulmus_metin += matrix[i][j]

    print(f"Çözülmüş metin: {cozulmus_metin}")


sifrele()
coz()




