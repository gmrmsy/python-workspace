#### 8일차 ####
'''
list
 하나의 자료형으로 여러개의 값을 저장할 수 있다
 []로 표현되면 리스트로 생각하면 어느정도 맞다
 각 각의 값에 접근하고자 할 경우 index를 이용한다.
 index는 0부터 시작한다.
 '''

ls = [500,200,300,400]
print(ls)
print(ls[0])
print(ls[3])
'''
ls = [0, 0, 0]
ls[0] = int(input('값 입력 : '))
ls[1] = int(input('값 입력 : '))
ls[2] = int(input('값 입력 : '))
sum_=ls[0] + ls[1] + ls[2]
print(ls)
print(sum_)
print('')
'''
ls = [0,0,0]
sum_=0
print( 'len :',len(ls) )

for i in range( len(ls) ) :
    # ls[i] = int(input(str(i),'값 입력 : ')) # input에는 값이 하나만 들어갈 수 있다.
                                                          # 쉼표쓰면 2개가 들어가기 때문에 못쓴다
    sum_ += ls[i]
print(ls)
print('합 :',sum_)

ls = [10, 20, 30, 40]
print('ls:',ls) # ><=
print(ls[1:3]) # 1시작 >3
print(ls[:2]) # >2
print(ls[1:]) # <=1
print(ls[:])

a = 10 ; b = 20 ;
print(a, b)
a, b = b, a
print(a,b)

ls = [4, 8, 2, 7, 6]
print(len(ls))
for i in range(len(ls)) :
    print('i =',i)
    for k in range(i+1, len(ls)) :
        print('k =',k)
        if ls[i] < ls[k] :
            pass
        elif ls[i] > ls[k] :
            ls[i], ls[k] = ls[k], ls[i]
print(ls)
print('')
'''
for i in range(len(ls)) :
    for k in range(i+1, len(ls)) :
        if ls[i] > ls[k] :
            pass
        elif ls[i] < ls[k] :
            ls[i], ls[k] = ls[k], ls[i]
print(ls)

'''
'''
score = [82, 85, 76, 79, 96]
rank = [0, 0, 0, 0, 0]

for i in range(len(score)) :
    rank[i] = 1
    for k in range(len(score)) :
        print(score[k])
        if score[i] > score[k] :
            pass
        elif score[i] < score[k] :
            rank[i] += 1
print(score)
print(rank)
'''
