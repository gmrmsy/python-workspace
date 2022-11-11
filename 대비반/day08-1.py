n = 100
print( n )
print( id(n)) # 정보값 출력
print('')

ls = [10, 20, 30]
arr = ls
print( id(ls) )
print( id(arr) ) # 두 정보값이 일치한다
                       # arr정보값 -> ls정보값 -> 정보공간
                       # 얕은 복사

ls[1] = 12345
print(ls)
print(arr) # ls를 변경했으나 같은 정보공간의 정보값을 쓰기 때문에 결과가 같다
print('')



ls = [10, 20, 30]
arr = ls[:]
print( id(ls) )
print( id(arr) ) # 정보값이 다르다
                       # ls를 복사한게 아니라 ls에 있는 정보를 arr에 가져와 변수를 새로만들었기 때문
                       # 깊은 복사
print('')

# import day01
import copy # 다른 페이지에 있는 값을 현재 페이지에 사용하려 할 때 import를 쓴다
ls = [10, 20, 30,]
arr = copy.deepcopy(ls) # 컨 + 스 / 명령어 기능
print( id(ls) )
print( id(arr) )
print('')


arr = ls.copy()
print( id(ls) )
print( id(arr) )
print('')



ls = [10, 20, 30]
arr = [40, 50, 60]
print(ls)
print(arr)
str_ = ls + arr
print(str_)
str_ = ls * 3
print(str_)

sum_ = [0, 0, 0]
mul_ = [0, 0, 0]
for i in range(len(ls)) :
    sum_[i] = ls[i]  +arr[i]


for i in range( len(ls) ) :
    mul_[i] = ls[i] * 3

print(ls)
print(mul_)













