# mükemmel sayı, bölenleri toplamı kendisine eşit olan sayılardır

sayi = int(input("Sayı giriniz: "))
sayinin_bolenleri = []
toplam = 0
i = 1
while i < sayi:
    if sayi % i == 0:
        sayinin_bolenleri.append(i)
        toplam = toplam + i
    i = i + 1
if toplam == sayi:
    print("Seçtiğiniz sayı bir mükemmel sayıdır")
else:
    print("Seçtiğiniz sayı mükemmel sayı değildir")



# ust_sinir = int(input("Üst sınırı giriniz: "))
#
# for i in range(1, ust_sinir + 1):
#     toplam = 0
#
#     for j in range(1, i):
#         if i % j == 0:
#             toplam = toplam + j
#
#     if toplam == i:
#         print("-> " + str(toplam))

