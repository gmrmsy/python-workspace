import os
os.system("cls") 
n = None
while True :
    print('='*40)
    print('1. 숫자 입력 (0 ~ 99)')
    print(f'2. 사이클 횟수 확인 (현재 숫자 : {n})')
    print(f'3. 사이클 과정 확인 (현재 숫자 : {n})')
    print('4. 종료')
    print('='*40)
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
        print()
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