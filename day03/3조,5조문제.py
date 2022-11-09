# 3조 3번

first = 10
money = 0

for i in range(30) :
    money += first
    first *= 2

print(money)





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
