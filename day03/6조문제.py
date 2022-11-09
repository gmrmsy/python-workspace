# 연재

num = 0

while True :
    print('='*40)
    print('1. 입력한 수까지의 합 계산 시작!')
    print('2. 끝내고 싶어!')
    print('='*40)
    select = int(input('>>>>>'))

    if select == 1 :
        n = 0
        plus = int(input('숫자를 입력하세요! '))
        print()
        for i in range(plus) :
            n += i
        print(f"1부터 {plus}까지의 합은 {n}입니다!'ㅁ' ")
        print()
    
    elif select == 2 :
        break

    else :
        print('정확한 메뉴를 선택해주세요!')
        print()


# 명진이

n = 0
for i in range(5,22,2) :
    n += i
print(f'4에서 21까지 홀수의 합은{n}입니다')


n = 0
for i in range(4,22) :
    if i % 2 == 1 :
        n += i
print(f'4에서 21까지 홀수의 합은{n}입니다')


# 명화누나

num = int(input('정수를 입력해주세요!'))

for i in range(1,num+1) :
    print('☆'*i)
