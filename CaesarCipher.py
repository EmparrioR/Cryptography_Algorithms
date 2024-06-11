alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

def sifrele():
    gönderilecek_mesaj = input("Mesajı Giriniz: ").replace(" ","").lower()
    

    sifreli_liste = []
    
    for s in gönderilecek_mesaj:
        if (s in alphabet):
            index = (alphabet.index(s)+3) % 29
            s = alphabet[index]
        sifreli_liste.append(s)

    sifreli_mesaj = "".join(sifreli_liste)
    print("Şifrelenmiş hali:", sifreli_mesaj)


def cöz():
    gelen_mesaj = input("Mesajı Giriniz: ")
    cözümlü_liste = []
    
    for s in gelen_mesaj:
        if (s in alphabet):
            s = alphabet[alphabet.index(s)-3]
        cözümlü_liste.append(s)

    cözülmüs_mesaj = "".join(cözümlü_liste)
    print("Çözülmüş Hali:", cözülmüs_mesaj)


sifrele()
cöz()