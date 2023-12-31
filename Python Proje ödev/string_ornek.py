# Kullanıcıdan bir cümle al ve alfabetik karakterlerin sayılarını döndüren bir algoritma oluştur

kelimeler=input("İstediğiniz kelimeleri veya cümleleri girin: ")
kelime = kelimeler.lower()

harfler = set()

for harf in kelime:
    if harf.isalpha():
        harfler.add(harf)

siralanmis_harfler = sorted(harfler)

for i in siralanmis_harfler:
    print(i + "->" + str(kelime.count(i)))
-+