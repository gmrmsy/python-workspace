import keyword
print( keyword.kwlist)
print()

# 해당 단어들은 키워드! 변수이름으로 사용하면 안된다!

num = 100
print( num )
print()

print('나의 나이는',20,'살 입니다.')
print('만으로는',20-1,'살 입니다.')
print('내년에는',20+1,'살 입니다.')
print()

n = 5
print('변경 전 n :',n)
n = n + 10
print(f'변경 후 n : {n}')
print()

n1 = 5 ; n2 = 10 ;
sum_ = n1 + n2
print(f'{n1}+{n2}={sum_}')
print()

n1 = 10
n2 = 20
sum_ = n1 + n2
print()

print('     --- 출력 결과 ---     ')
print('num1(',n1,') + num2(',n2,') =',sum_)
print(f'num1({n1}) + num2({n2}) = {sum_}')
print('num1({}) + num2({}) = {}'.format(n1, n2, sum_))
print()

flt = 123.456
print('flt :',flt)
print('round(flt) :',round(flt))
print('round(flt,1) :',round(flt,1))
print('round(flt,2) :',round(flt,2))
print()

python = 80
c = 70
java = 75
sum_ = python+c+java
avg = sum_/3

print(f'합계 : {sum_}\n평균 : {round(avg,2)}')
print()

sub = 11
time = 37

print(f'한 역당 평균시간 : {round(time/sub,2)}분')
print()

first = 500.23
floor = 260

print(f'건물의 총 높이는 : {round((first+floor*13)/100,3)}m')
print()