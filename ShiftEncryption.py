alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

def sifrele():
    gönderilecek_mesaj = input("Mesajı Giriniz: ")
    sifreli_liste = []
    
    key_value = int(input("Anahtar değeri giriniz: "))
    
    for s in gönderilecek_mesaj:
        if (s in alphabet):

            s = alphabet[(alphabet.index(s)+key_value) % 29]
        sifreli_liste.append(s)

    sifreli_mesaj = "".join(sifreli_liste)
    print("Şifrelenmiş hali: ", sifreli_mesaj)

def coz():
    gönderilecek_mesaj = input("Mesajı Giriniz: ")
    sifreli_liste = []
    
    key_value = int(input("Anahtar değeri giriniz: "))
    
    for s in gönderilecek_mesaj:
        if (s in alphabet):

            s = alphabet[(alphabet.index(s)-key_value) % 29]
        sifreli_liste.append(s)

    sifreli_mesaj = "".join(sifreli_liste)
    print("Çözülmüş hali: ", sifreli_mesaj)

sifrele()    
coz()