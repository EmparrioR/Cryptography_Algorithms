turkish_alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'

def sifrele():
    
    giris_metni = input("Lütfen Metni Giriniz: ")
    anahtar = input("Lütfen anahtar değer giriniz: ")
    metin = giris_metni.replace(" ","").lower()

    sifreli_metin = ""
    key_length = len(anahtar)
    key_index = 0

    for char in metin:
        if char.lower() in turkish_alphabet:
            # Hem büyük harf hem de küçük harf için çalışacak
            alphabet_index = turkish_alphabet.index(char.lower())
            # anahtarın karakter sayısına göre gruplama gerçekleştirir
            shift = turkish_alphabet.index(anahtar[key_index % key_length].lower())
            sifrelenmis_karakter_indexi = (alphabet_index + shift) % 29
            sifrelenmis_karakter = turkish_alphabet[sifrelenmis_karakter_indexi]

            # Eğer karakter büyük harfse, çıktıyı da büyük harfe çevir
            if char.isupper():
                sifrelenmis_karakter = sifrelenmis_karakter.upper()

            sifreli_metin += sifrelenmis_karakter
            key_index += 1
        else:
            sifreli_metin += char

    print(f"Şifreli Metin: {sifreli_metin}")


def coz():
   
    giris_metni = input("Lütfen Metni Giriniz: ")
    anahtar = input("Lütfen anahtar değer giriniz: ")
    metin = giris_metni.replace(" ","").lower()
    
    cozulmus_metin = ""
    key_length = len(anahtar)
    key_index = 0

    for char in metin:
        if char.lower() in turkish_alphabet:
            alphabet_index = turkish_alphabet.index(char.lower())
            shift = turkish_alphabet.index(anahtar[key_index % key_length].lower())
            cozulmus_karakter_indexi = (alphabet_index - shift) % 29
            cozulmus_karakter = turkish_alphabet[cozulmus_karakter_indexi]

            if char.isupper():
                cozulmus_karakter = cozulmus_karakter.upper()

            cozulmus_metin += cozulmus_karakter
            key_index += 1
        else:
            cozulmus_metin += char

    print(f"Çözülmüş Metin: {cozulmus_metin}")


sifrele()
coz()

