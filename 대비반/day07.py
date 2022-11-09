### 7일차 ###
'''
for i in range(1,1001, 1) :
    a = 0
    for k in range(1, 501, 1) :
        if i != k :
            if i % k == 0 :
                a += k
    if a == i :
        print(a)

for i in range(1, 1001):
    sum_ = 0
    j = 1
    while j < i:
        #print(f"{i} % {j} = { i % j }")
        if i % j == 0:
            sum_ += j
        j += 1
    if sum_ == i:
        print(f'{sum_}완전수 입니다')

'''
'''
num = int( input('수 입력 : ') )
for i in range(2, num+1):
    cnt = 0
    for j in range(1, i+1):
        #print(f"{i} % {j} = {i%j}")
        if i%j == 0:
            cnt += 1
    if cnt == 2:
        print(i," : 소수")
        
a = int(input('숫자를 입력하세요 : '))
for i in range(1, a+1, 1) :
    b = 0
    for k in range(1, a+1, 1 ) :
        if k != 1 :
            if  i % k == 0 :
                b += 1
    if b == 1 :
        print(i)

'''
line = 0

while line % 2 == 0 :
    line = int(input('홀수의 줄수를 입력 : '))
    if line % 2 == 0 :
        print('홀수를 입력하세요')


for i in range(1, line+1, 1) :
    if line // 2 +1 > i :
        star = '*' * (1 + (i-1)*2)
        print('{:^100}'.format(star))
    if line // 2 + 1 == i :
        star = '*' * (line)
        print('{:^100}'.format(star))
    if line // 2 + 1 < i :
        star = '*' * (1+(line-i)*2)
        print('{:^100}'.format(star))


ln = 5; flag =0; sp = ln//2; st=1;
i,j,num=0,0,1;
while num:
    ln = int(input('홀수의 줄수를 입력 : '))
    flag=0;    sp = ln//2;    st = 1;
    for i in range (ln):
        for j in range (sp):print(" ",end="")
        for j in range (st):print("*",end='')
        print()
        if i==(ln//2): flag=1
        if flag==0:    sp-=1; st+=2
        else:   sp+=1; st-=2
    num = int(input('0.종료 1.계속 : '))
print('프로그램 종료')



        
              

