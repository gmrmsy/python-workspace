'''
N = int(input('시간 입력>>> '))
count = 0
for j in range(N+1) :
    if j%10 == 3 or j//10 == 3 :
        count += 3600
        print(f'{j}시 {i}분 {k}초')
        continue
    for i in range(60) :
        if i%10 == 3 or i//10 == 3 :
            count += 60
            print(f'{j}시 {i}분 {k}초')
            continue
        for k in range(60) :
            if k%10 == 3 or k//10 == 3 :
                count += 1
                print(f'{j}시 {i}분 {k}초')
                continue
print(count)



n = int(input("시간 입력: "))
count=0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1
print("{}시59분59초까지 3이 하나라도 포함된 경우의 개수는 {}개 입니다.".format(n,count))


num = int(input('피라미드의 높이>>>>> '))

for i in range(1,num+1) :
    for j in range(num-i) :
        print('□',end='')
    for k in range(2*i-1) :
        print('■',end='')
    for l in range(num-i) :
        print('□',end='')
    print()


N = int(input('숫자를 입력하세요>>> '))
count = 0

for i in range(1,N+1) :
    count_ = 0
    for k in range(1,N+1) :
        if i % k == 0 :
            count_ += 1
    if count_ >= 3 :
        count += 1
        print(f'{i}는 합성수입니다')
print()    
print(f'합성수의 개수는 {count}개 입니다')


n = int(input('숫자>>> '))

for i in range(n) :
    print(' '*i,end='')
    print('*')

'''