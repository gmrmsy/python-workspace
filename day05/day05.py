'''
ls = [500, 200, 300, 400]
print( ls )
print( ls[0], ls[3] )




ls = [0, 0, 0, 0]
ls[0] = int(input('수 입력 : '))
ls[1] = int(input('수 입력 : '))
ls[2] = int(input('수 입력 : '))
ls[3] = int(input('수 입력 : '))

sum_ = ls[0]+ls[1]+ls[2]+ls[3]
print('합 :', sum_)




ls = [0, 0, 0, 0]
for i in range(len(ls)) :
    ls[i] = int(input('수 입력 : '))

sum_ = ls[0]+ls[1]+ls[2]+ls[3]
print('합 :', sum_)




ls = [0, 0, 0, 0]
i = 0
while i < len(ls) :
    ls[i] = int(input('수 입력 : '))
    i += 1

sum_ = ls[0]+ls[1]+ls[2]+ls[3]
print('합 :', sum_)
'''




ls = [ 10, 20, 30, 40, 50 ]

print(ls[2:])
print(ls[:2])
print()




# 얕은 복사 , 깊은복사

ls = [10, 20, 30, 40]
arr = ls                 # 얕은복사
print(ls,':',id(ls))     # 정보값 출력
print(arr,':',id(arr))   # 두 정보값이 일치한다
print()                  # arr정보값 -> ls정보값 -> 정보공간
                         

ls = [10, 20, 30, 40]    # 깊은복사
arr[0] = 90              # arr를 변경했으나 같은 정보공간의 정보값을 쓰기 때문에 결과가 같다
print(ls,':',id(ls))
print(arr,':',id(arr))
print()


ls = [10, 20, 30, 40]
arr = ls[:]
arr[0] = 90
print(ls,':',id(ls))     # 정보값이 다르다
print(arr,':',id(arr))   # ls를 복사한게 아니라 ls에 있는 정보를 arr에 가져와 변수를 새로만들었기 때문
print()                  # 깊은 복사




ls = [10, 20, 30]
arr = [40, 50, 60]

arr02 = ls + arr
print(arr02)

arr03 = ls * 3
print(arr03)

str = [0, 0, 0]
for i in range(len(ls)) :
    str[i] = ls[i] + arr[i]
print(str)

string = [0, 0, 0]
for i in range(len(ls)) :
    string[i] = ls[i] * 3
print(string)




ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32]
evenSum = []
oddSum = []

for i in range(len(ls)) :
    a = [ls[i]]
    if i % 2 == 0 :
        evenSum += a
    if i % 2 == 1 :
        oddSum += a

result = [0, 0, 0, 0, 0]
for i in range(len(evenSum)) :
    result[i] = evenSum[i] - oddSum[i]

print(result)

even = 0
odd = 0
for i in range(len(evenSum)) :
    even += evenSum[i]
    odd += oddSum[i]

print(even-odd)

invertLs = []
for i in range(len(ls)-1,-1,-1) : 
    a = [ls[i]]
    invertLs += a
    
print(ls)
print(invertLs)
print()


def sum_(group) :
    sum_ = 0
    for i in range(len(group)) :
        sum_ += group[i]
    
    return sum_

qwe = sum_(ls)
print(qwe)
print()

score = [82, 85, 76, 79, 96]


def sort_(score) :

    rank_ = []
    for i in range(len(score)) :
        rank_.append(1)

    for i in range(len(score)) :
        for k in range(len(score)) :
            if score[i] - score[k] >= 0 :
                pass
            elif score[i] - score[k] < 0 :
                rank_[i] += 1

    rank = {}
    for i in range(len(score)) :
        rank[rank_[i]] = score[i]
    
    return rank




a = sort_(score)

print(a)
print()
'''
# for i in :
#    print(a[i])

ls = list()
for i in range(3) :
    value = input(f'{i} 번째 입력 : ')
    ls.append(value)
print('총 개수 : :', len(ls))
print('type :', type(ls))
print('ls :', ls)
print()
'''

ls = []
print('초기화 후 ls :', ls)
print()

ls = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print('ls :',ls)
print()

a = ls.pop()    # ()번째 자료 뽑아내기, 빈칸은 맨뒤
print('pop :',ls)
print(a)
print()

a = ls.pop(1)
print('pop :',ls)
print(a)
print()


ls.reverse()
print('reverse :',ls)
print()

ls.sort()
print('sort :',ls)
print()


ls = [10, 50, 40, 30, 20]
arr = ls[:]
ls.reverse()
print(arr)
print(ls)

# sort_arr = arr.sort()  # 명령함과 동시에 변수설정 안된다!
# print(sort_arr)

sort_arr = ls[:]
sort_arr.sort()
print(sort_arr)

reverse_arr = ls[:]
reverse_arr.sort()
reverse_arr.reverse()
print(reverse_arr)

print()


ls = ['10', '20', '30']
print('변환전 :',ls)
s = list(map(int,ls))   # 그룹내에 자료형을 전부 바꿔준다
print('변환후 :',s)

ls = ['10', '20', '30']
s = map(int,ls)
print(s)    # list 안씌우면 map형태


ls = ['10', '20', '30']
s = []
for i in ls :
    s.append( int(i) )
print(s)

print()


# x = map(int, input().split())
# a, b = x
# print(a,' ',b)


a = [1,2,3,'4','5']

x = list(map(int,a[:4]))

print(list(x))


