sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))

sayi1nin_bolenleri = set()
i = 1
while i <= sayi1:
    if sayi1 % i == 0:
        sayi1nin_bolenleri.add(i)
    i = i + 1

sayi2nin_bolenleri = set()
i = 1
while i <= sayi2:
    if sayi2 % i == 0:
        sayi2nin_bolenleri.add(i)
    i = i + 1

ortak_bolenler = sayi1nin_bolenleri.intersection(sayi2nin_bolenleri)

ebob = max(ortak_bolenler)
ekok = (sayi1 * sayi2) / ebob

print(ebob)
print(int(ekok))
