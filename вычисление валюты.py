import time
s=0

while s != 1:
    time.sleep(2)
    print("Выбор Валют:")
    print("1.американский доллар")
    time.sleep(0.5)
    print("2.евро")
    time.sleep(0.5)
    print("3.британский фунт")
    time.sleep(0.5)
    print("4.японская иена")
    time.sleep(0.5)
    print("5.китайский юань")
    time.sleep(0.5)
    que=int(input("Какую валюту ты хочешь посчитать(напиши цифру от 1 до 5)? Если ты хочешь выйти пропиши здесь команду exit)\n>>>").lower())
    if que >= 3:
        if que == 3:
            fun = int(input("сколько Фунтов тебе нужно посчитать?\n>>>"))
            print(fun * 140, 'рублей')
        else:
            if que == 4:
                ien = int(input("сколько Иен тебе нужно посчитать?\n>>>"))
                print(ien * 1, 'рублей')
            else:
                if que == 5:
                    uan = int(input("сколько Юаней тебе нужно посчитать?\n>>>"))
                    print(uan * 17, 'рублей')
                else:
                    if que == 'exit':
                        s=+1
                        print("пока! возращайся снова!")


    else:
        if que == 2:
            eur=int(input("сколько Евро тебе нужно посчитать?\n>>>"))
            print(eur * 116, 'рублей')
        else:
            if que == 1:
                dol = int(input("сколько Долларов тебе нужно посчитать?\n>>>"))
                print(dol * 106, 'рублей')
            else:
                if que == 'exit':
                    s=+1
                    print("пока! возращайся снова!")



