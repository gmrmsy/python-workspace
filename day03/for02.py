
sum_ = 0
num1 = int(input("수 입력 : "))
num2 = int(input("수 입력 : "))
for i in range(num1, num2+1, 1):
    sum_ += i;
for i in range(num2, num1+1, 1):
    sum_ += i;
print( sum_ )

num1 = int(input("첫번째 수 입력 : "))
num2 = int(input("두번째 수 입력 : "))
if num1 > num2:
    max_, min_ = num1, num2
else:
    max_ = num2; min_ = num1;
sum_ = 0;
for i in range(min_,max_+1):
    sum_ += i;
print("범위안의 합 : ",sum_)


st = "Hello Python"

for i in "Hello Python":
    print(i)

st = "It is a fun Python class"
cnt_a = cnt_s = cnt = 0
for i in st:
    cnt+=1
    if i == 'a':
        cnt_a += 1
    elif i == 's':
        cnt_s += 1
print(f"총 개수 : {cnt}\na 개수:{cnt_a}\ns 개수:{cnt_s}")











