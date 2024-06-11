alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

def sifrele():
    gönderilecek_mesaj = input("Mesajı Giriniz: ").replace(" ","").lower()
    sifreli_liste = []
    
    # denklem = ax + y

    #x = int(input("X değerini giriniz: "))
    #y = int(input("Y değerini giriniz: "))
    
    x = 7
    y = 5 
    

    for s in gönderilecek_mesaj:
        
        if (s in alphabet):
            
            s = alphabet.index(s)
            index = (s*x + y) % 29
            s = alphabet[index]
        sifreli_liste.append(s)

    sifrelenmis_mesaj = "".join(sifreli_liste)
    print("Şifrelenmiş Mesaj: ", sifrelenmis_mesaj)

# Modüler aritmetik
def moduler_tersi(x, mod):
    for i in range(1, mod):
        if (i * x) % mod == 1:
            return i
    return None

def cöz():
    şifreli_mesaj = input("Mesajı Giriniz: ")
    şifreli_liste = []

    x = int(input("X değerini giriniz: "))
    y = int(input("Y değerini giriniz: "))
    
    çarpan_tersi = moduler_tersi(x, 29)

    for s in şifreli_mesaj:
        if (s in alphabet):
            s = alphabet.index(s)
            index = ((s - y) * çarpan_tersi) % 29
            s = alphabet[index]
        şifreli_liste.append(s)

    orijinal_mesaj = "".join(şifreli_liste)
    print("Orijinal Mesaj: ", orijinal_mesaj)


sifrele()    
cöz()