import numpy as np

alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def harf_to_index(harf):
    if harf in alfabe:
        return alfabe.index(harf)
    else:
        raise ValueError(f"'{harf}' karakteri Türkçe alfabede bulunmuyor.")

def index_to_harf(index):
    return alfabe[index]

def temizle_metin(metin):
    temizlenmis = ""
    for harf in metin:
        if harf in alfabe:
            temizlenmis += harf
    return temizlenmis

def hill_sifreleme():
    anahtar = []
    print("Lütfen 2x2 anahtar matrisini giriniz:")
    for i in range(4):
        anahtar.append(int(input(f"Eleman {i+1}: ")))
    
    acik_metin = input("Lütfen şifrelenecek metni giriniz: ").replace(" ", "").upper()
    acik_metin = temizle_metin(acik_metin)

    # Metin uzunluğunu çift yapmak için A ekliyoruz
    if len(acik_metin) % 2 != 0:
        acik_metin += "A"  
    
    matris_anahtar = np.array(anahtar).reshape(2, 2)
    sifreli_metin = ""
    
    for i in range(0, len(acik_metin), 2):
        matris_metin = np.array([harf_to_index(acik_metin[i]), harf_to_index(acik_metin[i+1])])
        matris_sifreli = np.dot(matris_anahtar, matris_metin) % len(alfabe)
        sifreli_metin += index_to_harf(matris_sifreli[0]) + index_to_harf(matris_sifreli[1])
    
    print("Şifreli Metin:", sifreli_metin)

def hill_cozme():
    anahtar = []
    print("Lütfen 2x2 anahtar matrisini giriniz:")
    for i in range(4):
        anahtar.append(int(input(f"Eleman {i+1}: ")))
    
    sifreli_metin = input("Lütfen şifrelenmiş metni giriniz: ").replace(" ", "").upper()
    sifreli_metin = temizle_metin(sifreli_metin)

    matris_anahtar = np.array(anahtar).reshape(2, 2)
    
    # matrisin determinantını alma
    det = int(np.round(np.linalg.det(matris_anahtar))) % len(alfabe)
    
    if det == 0 or gcd(det, len(alfabe)) != 1:
        print("Geçersiz anahtar matrisi. Determinant sıfır veya 29 ile aralarında asal değil.")
        return

    # Ters determinant alma 
    inv_det = mod_inverse(det, len(alfabe))
    
    matris_anahtar_ters = inv_det * np.round(np.linalg.inv(matris_anahtar) * det).astype(int) % len(alfabe)

    # Ters matrisi pozitif hale getirmek için mod 29 uygulayarak düzeltelim
    matris_anahtar_ters = np.mod(matris_anahtar_ters, len(alfabe))

    cozulen_metin = ""
    
    for i in range(0, len(sifreli_metin), 2):
        matris_metin = np.array([harf_to_index(sifreli_metin[i]), harf_to_index(sifreli_metin[i+1])])
        matris_cozulen = np.dot(matris_anahtar_ters, matris_metin) % len(alfabe)
        cozulen_metin += index_to_harf(matris_cozulen[0]) + index_to_harf(matris_cozulen[1])
    
    print("Çözülen Metin:", cozulen_metin)

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

# anahtar matrisinin determinantının uygun olup olmadığını ölçe için kullanılır 
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

hill_sifreleme()
hill_cozme()
