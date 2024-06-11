alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
new_alphabet = "iğtnjülrobpsdztynuşçeakgvmlöc"

def sifrele():
    mesaj = input("Lütfen Mesajı Giriniz: ")
    a = mesaj.replace(" ","").lower()
    
    sifreli = ""

    for i in a:
       alp_index = alphabet.index(i)
       yeni_harf = new_alphabet[alp_index]
       sifreli += yeni_harf

    print("Şifreli Mesaj:", sifreli)   
   
def coz():
    mesaj = input("Lütfen Mesajı Giriniz: ")
    b = mesaj.replace(" ","").lower()

    cözülmüs = ""

    for j in b:
        newalp_index = new_alphabet.index(j)
        asil_harf = alphabet[newalp_index]
        cözülmüs += asil_harf
    
    print("Çözülmüş Mesaj: ",cözülmüs)    

sifrele()   
coz() 