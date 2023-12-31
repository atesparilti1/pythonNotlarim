sayi=int(input("Sayı giriniz: "))
basamak_sayisi= len(str(sayi))
toplam=0
for num in str(sayi):
    toplam= toplam + int(num)**basamak_sayisi
if sayi==toplam:
    print("Seçtiğiniz sayı armstrong sayısıdır")
else:
    print("Seçtiğiniz sayı armstrong sayısı değildir")