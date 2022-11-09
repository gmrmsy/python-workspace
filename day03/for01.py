'''
반복문
- 어떤 내용을 반복하고자 하는 경우
- 규칙적으로 값이 변경 된다면
for 변수 in range(초기값, 비교값, 증감값):
    종속문장
'''
num = 0
num = num + 1; print(num)
num = num + 1; print(num)
num = num + 1; print(num)
num = num + 1; print(num)
num = num + 1; print(num)
num = num + 1; print(num)
num = num + 1; print(num)
num = num + 1; print(num)
num = num + 1; print(num)
num = num + 1; print(num)
print("="*20)

for i in range(0,11,1):#(i=0, i<11, i=i+1)
    print(i)
print('다음 문장 실행')

for i in range(1,11,1):#(i=1, i<11, i=i+1)
    print("----for 시작")
    if i % 2 == 0:
        print("i = ",i)
    print("for 종료----")

print("다음 문장 실행")
print("="*10)
for i in range(1, 11, 2):
    print(i)

print("안녕", end="aaa")
#print();print()
#print();print()
print("하세")
print("요")

for i in range(1, 11, 1):
    print(i, end=" ")



sum_ = 0
for i in range(1 , i < 11 , 1) :
    sum_ = sum_ + i
print("1 ~ 10 까지의 합 : ",sum_ )


for i in range(1,31,1):
    print(i,end="\t")
    if i%5==0:
        print()

odd_sum =0; even_sum=0
num = int(input("수 입력"))
for i in range(1, num+1, 1):
    if i %2 ==0:
        even_sum += i
    else:
        odd_sum += i
print(f"1~{num}까지의 짝 합 : {even_sum}")
print(f"1~{num}까지의 홀 합 : {odd_sum}")

print("="*10)
for i in range(0,10):
    print( i , end=", ")
print()
print("="*10)
for i in range( 10 ):
    print( i , end=", ")
print()













