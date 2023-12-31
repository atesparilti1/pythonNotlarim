print("\nasal sayi kontrolu\n")

while True:
    try:
        number = int(input("sayi giriniz : "))

        isPrime = True

        if number == 0:
            isPrime = False

        if number == 1:
            isPrime = False

        if number == 2:
            isPrime = True

        for i in range(2, number):
            if number % i == 0:
                isPrime = False
                break

        if isPrime:
            print("sayi asaldir")
        else:
            print("sayi asal degildir")

    except:
        print("sayi girmeliydiniz")
