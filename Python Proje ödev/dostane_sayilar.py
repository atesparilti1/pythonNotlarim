sayi1 = int(input("1.Sayıyı giriniz "))
sayi2 = int(input("2.Sayıyı giriniz "))
sayi1nin_bolenleri = []
i = 1
while i < sayi1:
    if sayi1 % i == 0:
        sayi1nin_bolenleri.append(i)
    i = i + 1
sayi1nin_bolenleri_toplami = sum(sayi1nin_bolenleri)
sayi2nin_bolenleri = []
i = 1
while i < sayi2:
    if sayi2 % i == 0:
        sayi2nin_bolenleri.append(i)
    i = i + 1
sayi2nin_bolenleri_toplami = sum(sayi2nin_bolenleri)
# print(sayi1)
# print(sayi1nin_bolenleri)
# print(sayi1nin_bolenleri_toplami)
# print(sayi2)
# print(sayi2nin_bolenleri)
# print(sayi2nin_bolenleri_toplami)

if sayi1nin_bolenleri_toplami==sayi2 and sayi2nin_bolenleri_toplami==sayi1:
    print("Seçtiğiniz sayılar dostane sayılardır")
else:
    print("Seçtiğiniz sayılar dostane sayılar değildir")




# number1 = int(input("ilk sayıyı giriniz: "))
# number2 = int(input("ikinci sayıyı giriniz: "))
#
# number1_bolenleri = set()
# number2_bolenleri = set()
#
# for i in range(1, number1):
#     if number1 % i == 0:
#         number1_bolenleri.add(i)
#
# for i in range(1, number2):
#     if number2 % i == 0:
#         number2_bolenleri.add(i)
#
# number1_bolenleri_toplami = sum(number1_bolenleri)
# number2_bolenleri_toplami = sum(number2_bolenleri)
#
# print(f"ilk sayının bölenleri toplamı: {number1_bolenleri_toplami}")
# print(f"ikinci sayının bölenleri toplamı: {number2_bolenleri_toplami}")
#
# if number1 == number2_bolenleri_toplami and number2 == number1_bolenleri_toplami:
#     print(f"{number1} ve {number2} sayıları dostane sayılardır")
# else:
#     print(f"{number1} ve {number2} sayıları dostane sayılar değildir")
