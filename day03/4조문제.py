# 1번
st = 'It is a fun python class'
a = 0

for i in st :
    a += 1

print(a)


# 2번

S = input('숫자를 입력하세요')
num = 0
for i in range(len(S)) :
    if i == 0 :
        num += int(S[i])
    elif i != 0 :
        if num == 0 :
            num += int(S[i])
        else :
            num *= int(S[i])

print(num)


# 3번

num = (input('숫자 5개를 공백을 두고 입력하세요\n'))
print()
N = num.split()

print(f'모든 숫자의 합은 {int(N[0])+int(N[1])+int(N[2])+int(N[3])+int(N[4])}입니다')
print(f'모든 숫자의 평균은 {(int(N[0])+int(N[1])+int(N[2])+int(N[3])+int(N[4]))/5}입니다')
print()


num = []

for i in range(5) :
    a = int(input(f'{i+1}번째 숫자를 입력하세요 : '))
    print()
    num.append(a)

sum_ = 0

for i in num :
    sum_ += i

print(f'모든 수의 합은{sum_}입니다.')
print(f'평균은 {sum_/5}입니다.')


# 4번

seat = 30
occupy = 0

while True :
    if seat > 0 :
        print('{:=^30}'.format('좌석 예약 프로그램'))
        print(f'잔여좌석 : {seat}석')
        num = int(input('인원수를 입력하세요 : '))
        if num > seat :
            print('좌석이 부족합니다')
            print()
        if num <= seat :
            print(f'{occupy+1}번부터 {occupy+num}번 좌석입니다')
            print()
            occupy += num
            seat -= num
    if seat == 0 :
        break
print('모든 좌석이 예약되었습니다. 예약을 종료합니다.')
print()
