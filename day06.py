##### 6일차 #####
'''
for i in range(0, 3, 1) :
    print('상위for문 실행')
    for k in range(0,5,1) :
        print(f'이중  for문 i:{i}, k:{k}')
    print('상위for문 종료')

for i in range(1,10,1) :
    print(f'{i}단')
    for k in range(1, 10, 1) :
        print(f'{i} X {k} = {i * k}')
'''

for i in range(0, 5, 1) :
    print(f'상위포문 {i} 일때 하위 포문 : ',end=' ')
    for k in range(0, 5, 1) :
        if k != 4 :
            print(f'{i*k}',end='  ')
        if k == 4 :
            print(f'{i*k}')

print('')            
        
for i  in range(1, 26, 5) :
    for k in range(0, 5, 1) :
        print(f'{i+k}',end='\t')
    print('')

print('')

i = 0
while i<5 :
    print(i,'종속문장실행')
    i += 1
print('다음 문장들 실행')

print('')

i=1
odd, even = 0, 0
while i <= 10 :
    if i % 2 == 0 :
        even += i
    else :
        odd += i 
    i += 1
print('1~10까지의 짝수 합 :', even)
print('1~10까지의 홀수 합 :', odd)

print('')

odd, even = 0, 0
for i in range(1, 11, 1) :
    if i % 2 == 0 :
        even += i
    else :
        odd += i
print('1~10까지의 짝수 합 :', even)
print('1~10까지의 홀수 합 :', odd)

print('')

i = 0
while i <5 :
    i += 1
    if i == 3:
        print('3333333')
        break
    print('i :',i)
print('다음 문장들 실행')

print('')

i = 0
while i <5 :
    i += 1
    if i == 3:
        print('3333333')
        # continue   # while 로 돌아가라!
    print('i :',i)

print('다음 문장들 실행')

print('')

i = 0
while i <5 :
    i += 1
    if i == 3:
        print('3333333')
        continue   # while 로 돌아가라!
    print('i :',i)
print('다음 문장들 실행')

print('')

rat = 2
rice = 100000
day = 0

while rice > 0 :
    day += 1
    rice -= (rat*20)
    if day % 10 == 0 :
        rat *= 2

print('총 쥐 마리수 :',rat , '소요 날짜 :',day)

print('')

C = 0
money = int(input('요금을 투입하세요 : '))

while C != 5 :
    print('{:=^45}'.format('커피 자판기'))
    print('1. 커피(200)  2. 코코아(250)  3. 요금추가  4. 반환  5. 종료\n')
    print(f'잔액 : {money}')
    C = int(input('메뉴를 선택하세요>>> : '))
    if C == 1 :
        num = int(input('수량을 입력하세요 : '))
        if money >= 200 * num :
            money -= 200 * num
            print('맛있게 드세요')
        else :
            print('요금이 부족합니다')
    elif C == 2 :
        num = int(input('수량을 입력하세요 : '))
        if money >= 250 * num :
            money -= 250 * num
            print('맛있게 드세요')
        else :
            print('요금이 부족합니다')
    elif C == 4 :
        print('반환 금액 :',money)
        money -= money
    elif C == 3 :
        money += int(input('요금을 투입하세요 : '))
    elif C == 5 :
        pass
    else :
        print('정확하게 입력해주세요')
    print('')
        
    
    
