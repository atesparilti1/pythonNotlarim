tek_sayilar = []
cift_sayilar = []

i = 1

while i < 101:
    if i % 2 == 0:
        cift_sayilar.append(i)
    else:
        tek_sayilar.append(i)
    i += 1

print("tek sayılar: " + str(tek_sayilar))
print("çift sayılar: " + str(cift_sayilar))