'''
N = int(input('수를 입력하세요 : '))
for i in range(1,10) :
    print(f'{N}X{i}={N*i}')


T = 0
N = int(input('계산 횟수를 입력하세요 : '))


while T != N :
    A = int(input('첫 번째 수를 입력하세요 : '))
    B = int(input('두 번째 수를 입력하세요 : '))
    print(f'{A} + {B} = {A+B}')
    T += 1
print('완료')


N = int(input('계산 횟수를 입력하세요 : '))
while T != N :
    A = input('두 숫자를 공백을 두고 입력하세요 : ')
    B = A.split()
    print(f'{int(B[0])} + {int(B[1])} = {int(B[0])+int(B[1])}')
    T += 1
print('완료')

num = int(input('수를 입력하세요 : '))
A = 0


for i in range(1, num+1) :
    A += i
print(A)


X = int(input('영수증의 총 금액을 입력하세요 : '))
N = int(input('물품 종류의 갯수를 입력하세요 : '))
price = 0
for i in range(1,N+1) :
    a = int(input(f'{i}번째 물품의 금액을 입력하세요 : '))
    b = int(input(f'{i}번째 물품의 수량을 입력하세요 : '))
    price += a*b

if X == price :
    print('yes')
if X != price :
    print('no')


N = int(input('줄 갯수를 입력하세요 : '))
for i in range(1,N+1) :
    print('*'*i)


N = int(input('줄 갯수를 입력하세요 : '))
for i in range(1,N+1) :
    print(str('*'*i).rjust(N))

'''

import os
os.system("cls") 
n = None
while True :
    print('='*32)
    print('1. 0~99 입력')
    print(f'2. 사이클 확인 (현재 숫자 : {n})')
    print(f'3. 사이클 과정 (현재 숫자 : {n})')
    print('4. 종료')
    print('='*32)
    num = int(input('>>>>>'))
    if num == 1 :
        N = int(input('숫자를 입력하세요 : '))
        print()
        n = N
        time = 0
        while True :
            if 99 < N or N < 0 :
                print('잘못된 숫자를 입력하셨습니다.')
                N = int(input('숫자를 입력하세요 : '))
                print()
            elif 0 <= N < 100 :
                new = (N//10) + (N%10)
                N = ((N%10)*10) + (new%10)
                time += 1
            if N == n :
                break

    elif num == 2 :
        print(f'{n}의 사이클횟수는 {time}회 입니다')
        os.system("pause")
        print()

    elif num == 3 :
        print(f'최초숫자A : {N}')
        new = (N//10) + (N%10)
        print(f'새로운수B : {N//10} + {N%10} = {new}')
        print(f'{(N%10)} {new%10}<------------┘----┘')
        N = ((N%10)*10) + (new%10)
        time = 1
        print(f'{time}회')
        while True :
            print(f'기준숫자A : {N}')
            new = (N//10) + (N%10)
            print(f'새로운수B : {N//10} + {N%10} = {new}')
            print(f'{(N%10)} {new%10}<------------┘----┘')
            N = ((N%10)*10) + (new%10)
            time += 1
            print(f'{time}회')
            print()
            if N == n :
             break
        os.system("pause")
        print()
    
    
    elif num == 4 :
        break
    os.system("cls") 

'''

N = int(input('숫자를 입력하세요 : '))
time = 1
n = N
while 99 < N or N < 0 :
    print('잘못된 숫자를 입력하셨습니다.')
    N = int(input('숫자를 입력하세요 : '))

new = ((N//10)) + (N-((N//10)*10))

N = ((N-((N//10)*10))*10) + (new-((new//10)*10))
 
while N != n :
    if N < 100 :
        if N > 9 :
            new = ((N//10)) + (N-((N//10)*10))
            N = ((N-((N//10)*10))*10) + (new-((new//10)*10))
        elif 0 < N < 10 :
            N = (N*10) + N
    
    time += 1

print(f'{n}의 사이클횟수는 {time}회')



import os
os.system("cls") 
n = None
while True :
    print('='*32)
    print('1. 0~99 입력')
    print(f'2. 사이클 확인 (현재 숫자 : {n})')
    print(f'3. 사이클 과정 (현재 숫자 : {n})')
    print('4. 종료')
    print('='*32)
    num = int(input('>>>>>'))
    if num == 1 :
        N = int(input('숫자를 입력하세요 : '))
        print()
        n = N
        time = 0
        while True :
            if 99 < N or N < 0 :
                print('잘못된 숫자를 입력하셨습니다.')
                N = int(input('숫자를 입력하세요 : '))
                print()
            elif 0 <= N < 100 :
                new = (N//10) + (N%10)
                N = ((N%10)*10) + (new%10)
                time += 1
            if N == n :
                break

    elif num == 2 :
        print(f'{n}의 사이클횟수는 {time}회 입니다')
        os.system("pause")
        print()

    elif num == 3 :
        print(f'최초숫자A : {N}')
        new = (N//10) + (N%10)
        print(f'새로운수B : {N//10} + {N%10} = {new}')
        print(f'{(N%10)} {new%10}<------------┘----┘')
        N = ((N%10)*10) + (new%10)
        time = 1
        print(f'{time}회')
        while True :
            print(f'기준숫자A : {N}')
            new = (N//10) + (N%10)
            print(f'새로운수B : {N//10} + {N%10} = {new}')
            print(f'{(N%10)} {new%10}<------------┘----┘')
            N = ((N%10)*10) + (new%10)
            time += 1
            print(f'{time}회')
            if N == n :
             break
        os.system("pause")
        print()
    
    
    elif num == 4 :
        break
    os.system("cls") 
'''