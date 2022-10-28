##### 9일차 #####
# list 기능

ls = [1, 2, 3, 4, 5]

ls.append(6) # list 추가
print(ls)

ls.pop(0) # 해당 값 추출 (비복원)
print(ls)
print(ls.pop(0))

ls.sort() # list 정렬
print(ls)

del( ls[3] ) # list명령어X , 데이터 삭제
print(ls)

result = ls.index(4) # 해당 데이터 찾기
print(result)

#result = ls.index(10)
print(result) 

ls.append(3)
result = ls.count(3) # 해당 데이터 갯수
print(result)


ls.insert(2,100)
print(ls)

ls.remove(100) # list 명령어O, 데이터 삭제

ls01 = [10, 20, 30]
ls02 = [40, 50, 60]
ls = ls01 + ls02
print(ls)

ls01.extend( ls02 )
print(ls01)

ls01 = [10, 20, 30]
ls02 = [40, 50, 60]
ls = ls02 + ls01
print(ls)

ls02.extend( ls01 )
print(ls02)

'''
num = 0
name = []
while num != 4 :
    num = int(input('1. 이름저장   2. 모든 이름 출력   3. 특정 이름 삭제   4. 종료'))
    if num == 1 :
        name_a = input('저장할 이름을 입력하세요 : ')
        if name.count(name_a) == 1 :
            print('존재하는 이름입니다')
        else :
            name.append(name_a)
    elif num == 2 :
        print(name)
    elif num == 3 :
        name_r = input('삭제할 이름을 입력하세요 : ')
        if name.count(name_r) == 1 :
            name.remove(name_r)
            print('삭제 성공')
        else :
            print('존재하지 않는 이름입니다')
'''
            
''' 
ls = ['김개똥', '2002년입사', '잘못된 사항', '등급B']

ls.remove(input('지울 값 입력 : '))
for i in range(1, 4) :
    ls.append(input('추가할 이름 입력 ; '))
    ls.append('2002년입사')
    ls.append('등급B')

for i in range(0, 4) :
    print(ls[i*3:(i+1)*3])              
'''

ls = [100, 200, [7,8,9]]

print( ls[2] )
print( ls[2][1] )


ls = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(ls)
print( ls[0][0])
print( ls[0][1])
print( ls[0][2])
print( ls[1][0])
print( ls[1][1])
print( ls[1][2])
print( ls[2][0])
print( ls[2][1])
print( ls[2][2])

for i in range(3) :
    for k in range(4) :
        if k == 3 :
            print(ls[i][k],end='\n')
        else :
            print(ls[i][k],end='\t')
            
