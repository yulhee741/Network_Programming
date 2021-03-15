from random import randint

money = 50

while 1:
    if money <= 0:
        break
    elif money >= 100:
        break
    else:
        coin = randint(1,2)
        print("동전의 앞면은 1, 뒷면은 2 입니다. 동전을 맞춰보세요!")
        res = int(input())
        if res == coin:
            print("맞췄습니다! 9달러를 획득했습니다.")
            money += 9
            print("현재금액은", money)
        else:
            print("틀렸습니다! 10달러를 잃었습니다.")
            money -= 10
            print("현재금액은", money)

print("게임이 종료되었습니다.")