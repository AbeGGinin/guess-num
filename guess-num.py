#產生一個隨機整數 1~100 不印出來
#讓使用者重複輸入數字去猜
#猜對的話 印出'終於猜對了'
#猜錯的話 要告訴他 比答案大/小
import random
r = random .randint(1, 100)
while True:
    a = input('請輸入數字(1~100):')
    a = int(a)
    if a == r:
        print('終於猜對了！')
        break
    else:
        if a != r and a > r:
            print('比答案小')
        else:
            print('比答案大')


        