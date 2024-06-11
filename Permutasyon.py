def sifrele():
    mesaj = input("Lütfen Mesajı Giriniz: ")
    key = input("Lütfen key değerini giriniz: ")
    a = mesaj.replace(" ", "").lower()
    key_length = len(key)
    new_list = []

    
    for i in range(0, len(a), key_length):
        block = a[i:i+key_length]
        if len(block) < key_length:
            block += "x" * (key_length - len(block))  
        new_list.append(block)

    sifrelenmis_metin = ""
    
    for block in new_list:
        for index in key:
            sifrelenmis_metin += block[int(index) - 1]

    print(f"Şifrelenmiş Mesaj: {sifrelenmis_metin}")

def coz():
    sifreli_metin = input("Lütfen şifreli metni giriniz: ")
    key = input("Lütfen key değerini giriniz: ")
    key_length = len(key)
    blocks = [sifreli_metin[i:i + key_length] for i in range(0, len(sifreli_metin), key_length)]

   
    index_map = {int(k) - 1: i for i, k in enumerate(key)}
    reverse_index_map = {v: k for k, v in index_map.items()}

    cozulmus_metin = ""
    
    for block in blocks:
        temp_block = [''] * key_length
        for i in range(len(block)):
            pos = reverse_index_map[i]
            temp_block[pos] = block[i]
        cozulmus_metin += ''.join(temp_block).rstrip('x')

    print(f"Çözülmüş metin: {cozulmus_metin}")


sifrele()
coz()