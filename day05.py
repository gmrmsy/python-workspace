##### 5일차 #####
'''
반복문
for(초기값, 비교값, 증감값) :
    종속문장
반복문
- 동일한 반복을 할 경우 사용
- 규칙적으로 값이 변하는 경우
- 여러개의 값을 하나씩 표현하고자 하는 경우
'''
'''
i = 1 ;
print( i )
i += 1
print( i )
'''
for i in range(1, 11, 1) : # for 대입명령어 in range(초기값, 비교값, 증감값) : / i+1, i<11, i+=1
    print( i )
print('다음 문장들 진행')
print('\n')

for i in range(1, 11, 1) :
    if i % 2 == 0 :
        print('i = ',i)
print('다음 문장들 실행')
print('\n')

print( 1 ) # 기본적으로 엔터값이 들어있다
print( 1, end='aaaa') # 엔터값 대신 넣을 값을 정한
print( 1 )
print('\n')

sum_ = 0
num = 1

for i in range(1, 11, 1) :
    sum_ = sum_ + num
    num += 1
print(sum_)
print('\n')

num = 0

for i in range(1, 31, 1) :
    num += 1
    if i%5 == 0 :
        a = '\n'
    else :
        a = '\t'
    print(num, end=f'{a}')
print('\n')
'''
num = int(input('수를 입력하세요 : '))
num_0 = 0
num_1 = 0

for i in range(0, num, 1) :
    i += 1
    if i%2 == 0 :
        num_0 += i
    if i%2 == 1 :
        num_1 += i
    print(f'i = {i}')
print('\n')
print(f'짝수의 합 : {num_0}')
print(f'홀수의 합 : {num_1}')
'''

a = 0

for i in range(1, 101, 1) :
    if i % 3 == 0 :
        if i % 5 == 0 :
            a += i
            print(a)
        else :
            pass
    else :
        a += i
        print(a)

'''
num_1 = int(input('첫 번째 숫자를 입력하세요 : '))
num_2 = int(input('두 번째 숫자를 입력하세요 : '))
sum_1 = 0
sum_2 = 0

for i in range(1, num_1+1, 1) :
    print(f'{i}')
    sum_1 += i
for i in range(1, num_2+1, 1) :
    print(f'{i}')
    sum_2 += i
print(f'{sum_1}', f'{sum_2}')
'''
'''
sum_ = 0

for i in range(1, 31) :
    if i == 1 :
        money = 10
    else :
        money *= 2
        
print(money)

'''

st = 'Hello Python'
for i in st :
    print(i)

st = 'It is a fun Python class'

a_ = 0
s_ = 0
n_ = 0

for i in st :
    if i == 'a' :
        a_ += 1
    if i == 's' :
        s_ += 1
    n_ += 1

print(f'a의 개수 : {a_}')
print(f's의 개수 : {s_}')
print(f'총 개수 : {n_}')
