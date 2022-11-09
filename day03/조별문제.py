# 3조 3번

first = 10
money = 0

for i in range(30) :
    money += first
    first *= 2

print(money)
print()





# 1조 1번

n = input('숫자를 입력하세요')
answer = 0

for i in n :
    if int(n) % 2 == 0 :
        if int(i) % 2 == 0 :
            answer += int(i)
    if int(n) % 2 == 1 :
        if int(i) % 2 == 1 :
            answer += int(i)

print(f'정답은 {answer}')
print()




# 1조 2-1번

num = 0
for i in range(1,32) :
    if i % 7 == 6 :
        print(f'{i}일은 분리수거 날입니다')
        num += 1
print(f'이번달 분리수거는 총 {num}회 있습니다.')
print()




# 1조 2-2번

n = int(input('숫자를 입력하세요 : '))
n3 = 0
n5 = 0
sum_3 = 0
sum_5 = 0

for i in range(n+1) :
    if i % 3 == 0 and i % 5 == 0 :
        pass
    elif i % 3 == 0 or i % 5 == 0 :
        if i % 3 == 0 :
            sum_3 += i
            n3 += 1
        if i % 5 == 0 :
            sum_5 += i
            n5 += 1
print(f'3의 배수의 개수는 {n3}개, 총 합은 {sum_3}입니다.')
print(f'5의 배수의 개수는 {n5}개, 총 합은 {sum_5}입니다.')