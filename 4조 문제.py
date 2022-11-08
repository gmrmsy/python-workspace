# 문제1

training_day = int(input('훈련 참석 일수를 입력하세요 : '))

if 0 <= training_day < 31 :
    if training_day/30 > 0.8 :
        money = training_day*15800
        print(f'지급받으실 훈련장려금은 {money}원 입니다.')
    else :
        print('꽁돈 받을 생각만 하지말고 공부 열심히 하거라')
else :
    print('올바른 날짜를 입력하세요')


# 문제2

money = int(input('승차권 구매 금액을 입력하세요 : '))
way = int(input('환불 수단을 선택하세요 [1. 현금환불  2. 할인증]'))
time = int(input('지연 시간을 입력하세요 : (분)'))

if time >= 60 :
    if way == 1 :
        reward = money * 1.5
    elif way == 2 :
        reward = money * 2
elif time >= 40 :
    if way == 1 :
        reward = money * 1.25
    elif way == 2 :
        reward = money * 1.5
elif time >= 20 :
    if way == 1 :
        reward = money * 1.125
    elif way == 2 :
        reward = money * 1.25
elif time < 20 :
    print('지원배상금이 없습니다')
print(f'지원배상금은 {reward}원 입니다.')


# 문제3

month = int(input('해당 월을 입력하세요 : '))

if month == 2 :
    print(f'{month}월은 28일까지 있습니다.')
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
    print(f'{month}월은 31일까지 있습니다.')
if month == 4 or month == 6 or month == 9 or month == 11 :
    print(f'{month}월은 30일까지 있습니다.')


# 문제4

apple = int(input('구입할 사과의 개수를 입력하세요 : '))
pear = int(input('구입할 배의 개수를 입력하세요 : '))
money = int(input('소지한 금액을 입력하세요 : '))
price = (apple*3000) + (pear*2000)

if price <= money :
    print(f'구매 성공! 잔액은 {money-price}원 입니다')
if price > money :
    print(f'구매불가 {price-money}원이 부족합니다.')