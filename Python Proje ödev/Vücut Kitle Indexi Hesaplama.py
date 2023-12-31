name=input("İsminiz: ")
print("Hoşgeldin Uygulamamıza " + name + " Vücut kitle indeksini ölçelim")

kilo=float(input("Kilonuz: "))

boy=float(input("Boyunuz (metre cinsinden) : "))

sonuç= str(kilo/(boy*boy))
sonuç1=(kilo/(boy*boy))

print("Vücut kitle indeksin " + sonuç)
if sonuç1<18:
    print("Zayıfsın yemek ye ")
elif sonuç1<25:
    print("Kilon iyi aferin")
elif sonuç1<30:
    print("Kilolusun biraz diet yap")
else:
    print("Şişman herif bu kilo ne git kilo ver ")