değer= input("Sayı giriniz:  ")
sayı = int(değer)

i = sayı - 1
if sayı == 2:
    print("Seçtiğin sayı asal")
    exit()
if sayı == 0 or sayı == 1:
    print("Asal değil")
    exit()
while i > 0:
    result = sayı / i
    # print(result) //
    if int(result) == result:
        print("Asal değil")
        break
    else:
        i -= 1
    if i == 1:
        print("Seçtiğin sayı asal")
        break
