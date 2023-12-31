n=int(input("Faktöriyel hesaplamak istediğiniz sayıyı giriniz: " ))
faktoriyel= 1
for num in range(1,n+1):
    faktoriyel= faktoriyel*num

print(faktoriyel)

# recursive
def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)


a = factorial(4)

print(a)

