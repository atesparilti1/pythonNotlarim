# Girilen bir ismin veya kelimenin Büyük Unlu Uyumuna uyup uymadığını kontrol eden bir algoritma oluştur

while True:
    kelime = input("Kelime giriniz: ")

    kalin = False
    ince = False

    kalin_str = 'aoıu'
    ince_str = 'eiüö'

    if kelime.isalpha():
        for index in kelime:
            for i in kalin_str:
                if index == i:
                    kalin = True
            for z in ince_str:
                if index == z:
                    ince = True

        if kalin and ince and kelime.isalpha():
            print("Büyük ünlü uyumuna uymaz")
        else:
            print("Büyük ünlü uyumuna uyar")
    else:
        print("Kelime giriniz")