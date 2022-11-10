'''
for i in range(0,3,1) :
    for k in range(0,5,1) :
        print(f'이중 for 문 (i:{i}, k:{k})')


for i in range(1,10) :
    for k in range(1,10) :
        print(f'{i} X {k} = {i*k}')


for i in range(5) :
    print(f'상위포문 {i} 일때 하위 포문 :',end=' ')
    for k in range(5) :
        if k != 4 :
            print(f'{i*k}',end=' ')
        if k == 4 :
            print(f'{i*k}')

for i in range(5) :
    for k in range(1,5) :
        print(f'{(i*5)+k}',end='\t')
    print(f'{(i+1)*5}')


i = 0
while i < 5 :
    i += 1
    if i == 3 :
        #continue
        #break
        print('333333')
    print(i, '.출력')
print()



i = 0
while i < 5 :
    print(f'{i, i, i}')
    if i == 2 :
        print('22')
    i += 1
else :
    print('?')



key = True

while key == True :
    no = int(input('숫자를 입력하세요 : '))
    print()

    while 10 <= no <= 20 :
        num = 0
        for i in range(no+1) :
            num += i
        print(num)
        break
    else :
        continue

    key = False



for i in range(0,3,1) :
    for k in range(0,5,1) :
        if k == 3 :
            break
        print(f'i : {i}, k : {k}')

print()

key = True 
while key == True :
    i = 0
    while i <= 2 :
        k = 0
        while k <= 4 :
            while k != 3 :
                print(f'i ; {i}, k : {k}')
                k += 1
            else :
                break
        i += 1
    else :
        break

print()

i = 0
while i <= 2 :
    k = 0
    while k <= 4 :
        while k != 3 :
            print(f'i ; {i}, k : {k}')
            k += 1
        else :
            break
    i += 1
'''
import os

key = 0

money = int(input('요금을 투입 하세요 : '))
while key != 5 :
    os.system("cls")
    print(f'잔액 : {money}원')
    print('{:=^58}'.format(' 커피 자판기 '))
    print('1. 커피(200)  2. 코코아(250)  3. 요금추가  4. 요금반환  5. 종료')
    print()
    key = int(input('메뉴를 선택하세요>>> '))
    print()

    if key == 1 :
        if money >= 200 :
            print('맛있게 드세요')
            os.system("pause")
            print()
            money -= 200
        elif money < 200 :
            print('요금이 부족합니다')
            os.system("pause")
            print()

    elif key == 2 :
        if money >= 250 :
            print('맛있게 드세요')
            os.system("pause")
            print()
            money -= 250
        elif money < 250 :
            print('요금이 부족합니다')
            os.system("pause")
            print()

    elif key == 3 :
        money += int(input('요금을 투입 하세요 : '))
        print(f'잔액 : {money}원')
        os.system("pause")
        print()            

    elif key == 4 :
        print(f'반환 금액 : {money}원')
        money -= money
        os.system("pause")
        print()
    
    elif key ==5 :
        pass
    else :
        print('번호를 다시 입력해주세요')
    