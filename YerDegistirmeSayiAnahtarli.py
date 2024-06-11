def sifrele():
    mesaj = input("Lütfen Mesajı Giriniz: ")
    key = int(input("Lütfen key değerini giriniz: "))
    a = mesaj.replace(" ", "").lower()
    
    columns = key
    
    bos_alan = columns - len(a) % columns
    a += 'a' * bos_alan 
     
    matrix = [a[i:i + columns] for i in range(0, len(a), columns)]
    
    key_order = sorted(range(columns)) 
    
    sifrelenmis_mesaj = ''
    for column in key_order:
        for row in matrix:
            sifrelenmis_mesaj += row[column]
    
    print(f"Şifrelenmiş Mesaj: {sifrelenmis_mesaj}")

def coz():
    mesaj = input("Lütfen Mesajı Giriniz: ")
    key = int(input("Lütfen key değerini giriniz: "))
    a = mesaj.replace(" ","").lower()

    # sütun sayısı anahtar değerine eşittir
    columns = key
    
    rows = len(mesaj) // key

    matrix = ['' for _ in range(columns)]
    index = 0
    for column in range(columns):
        for row in range(rows):
            if index < len(a):
                matrix[column] += mesaj[index]
                index += 1

    cozulmus_mesaj = ''
    for row in range(rows):
        for column in matrix:
            cozulmus_mesaj += column[row]

    padding_char = "a"
    if padding_char in cozulmus_mesaj:
        cozulmus_mesaj = cozulmus_mesaj.rstrip(padding_char)        

    print(f"Çözülmüş Mesaj: {cozulmus_mesaj}")



sifrele()
coz()