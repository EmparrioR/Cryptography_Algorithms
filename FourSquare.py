def anahtar_tablosu_olustur(anahtar):
    alfabe = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    tablo = []
    for harf in anahtar:
        if harf not in tablo and harf in alfabe:
            tablo.append(harf)
    for harf in alfabe:
        if harf not in tablo:
            tablo.append(harf)
    return [tablo[i:i+5] for i in range(0, 25, 5)]

def sifrele(anahtar1, anahtar2, metin):

    tablo1 = anahtar_tablosu_olustur(anahtar1)
    tablo2 = anahtar_tablosu_olustur(anahtar2)
    
    sifreli_metin = ""
    metin = metin.replace(" ", "").upper()
    
    
    if len(metin) % 2 != 0:
        metin += "X"
    
    for i in range(0, len(metin), 2):
        a, b = metin[i], metin[i+1]
        
        a_indis = [(ind, row.index(a)) for ind, row in enumerate(tablo1) if a in row][0]
        b_indis = [(ind, row.index(b)) for ind, row in enumerate(tablo2) if b in row][0]
        
        sifreli_metin += tablo2[a_indis[0]][b_indis[1]] + tablo1[b_indis[0]][a_indis[1]]
    
    return sifreli_metin

def coz(anahtar1, anahtar2, sifreli_metin):
    
    tablo1 = anahtar_tablosu_olustur(anahtar1)
    tablo2 = anahtar_tablosu_olustur(anahtar2)
    
    cozulen_metin = ""
    sifreli_metin = sifreli_metin.replace(" ", "").upper()
    
    for i in range(0, len(sifreli_metin), 2):
        a, b = sifreli_metin[i], sifreli_metin[i+1]
        
        a_indis = [(ind, row.index(a)) for ind, row in enumerate(tablo2) if a in row][0]
        b_indis = [(ind, row.index(b)) for ind, row in enumerate(tablo1) if b in row][0]
        
        cozulen_metin += tablo1[a_indis[0]][b_indis[1]] + tablo2[b_indis[0]][a_indis[1]]
    
    return cozulen_metin

# Kullanıcı girdisi ile şifreleme ve çözme
def sifrele_kullanici_girdisi():
    print("ŞİFRELE")
    print("Örnek anahtar: ANOTHERKEYWORDQWERTYUIOPASDFGHJKLZ")
    
    anahtar1 = input("Lütfen 1. anahtarı giriniz: ").replace(" ", "").upper()
    anahtar2 = input("Lütfen 2. anahtarı giriniz: ").replace(" ", "").upper()
    
    metin = input("Lütfen metni giriniz: ").replace(" ", "").upper()
    
    sifreli_metin = sifrele(anahtar1, anahtar2, metin)
    print("Şifreli Metin:", sifreli_metin)

def coz_kullanici_girdisi():
    print("ÇÖZ")
    print("Örnek anahtar: ANOTHERKEYWORDQWERTYUIOPASDFGHJKLZ")
    
    anahtar1 = input("Lütfen 1. anahtarı giriniz: ").replace(" ", "").upper()
    anahtar2 = input("Lütfen 2. anahtarı giriniz: ").replace(" ", "").upper()
    
    sifreli_metin = input("Lütfen metni giriniz: ").replace(" ", "").upper()
    
    cozulen_metin = coz(anahtar1, anahtar2, sifreli_metin)
    print("Çözülen Metin:", cozulen_metin)

sifrele_kullanici_girdisi()
coz_kullanici_girdisi()
