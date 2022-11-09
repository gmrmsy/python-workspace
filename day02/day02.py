flt = 123.456
print(round( flt + 100 ,3 ))
print()

st1, st2 = '파', '이썬'
print(st1+st2)
print()

# print( st1 + flt ) 서로 다른 자료형 연산 불가능!
# print( '100' + 100 ) 서로 다른 자료형 연산 불가능!
print()

num = 100
print(type(num))
print()

num = '100'
print(type(num))
print()

num = 123.456
print(type(num))
print()

num = '100'
print(int(num)+100)
print()

su = 100
num = '100'
flt = '1.111'

print(su+int(num))
print(su+float(flt))
print(str(su)+num)
print(su+int(float((flt))))  # '실수'는 바로 int처리 안됨, float처리 후 int가능
print()
'''
num1 = input('수 입력 : ')
print('입력 값 :',num1)

name = input('이름 입력 : ')
age = input('나이 입력 : ')
print(f'결과 출력 : {name}님의 나이는 {age}살 입니다')


name = input('학생이름 : ')
K = input('국어점수 : ')
E = input('영어점수 : ')
M = input('수학점수 : ')
sum_ = int(K)+int(E)+int(M)
avg = sum_ / 3

# print(f'학생이름 : {name}\n국어점수 : {K}\n영어점수 : {E}\n수학점수 : {M}')
print('{:=^42}'.format('학생 정보'))
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*46)
print(f'{name}\t{K}\t{E}\t{M}\t{sum_}\t{round(avg,2)}')
print()


num = int(input('숫자 입력 : '))

if num > 0 :
    print( num )
if num < 0 :
    print(f'{-num}' )



n1 = input('첫 번째 숫자 : ')
n2 = input('두 번째 숫자 : ')
n3 = input('세 번째 숫자 : ')

if n1 > n2 and n1 > n3 :
    print('n1이 제일 크다')

if n2 > n1 and n2 > n3 :
    print('n2가 제일 크다')
    
if n3 > n1 and n3 > n3 :
    print('n3이 제일 크다')

'''

save_id = ['asdf', 'zxcv', 'qwer', 'tyui', 'ghjk', 'vbnm']
save_id.append(input('저장할 아이디를 입력하세요 : '))
save_pw = {'asdf':1234, 'zxcv':2345, 'qwer':3456, 'tyui':4567, 'ghjk':5678, 'vbnm':6789}
save_pw[save_id[-1]] = int(input("비밀번호를 입력하세요 : "))

print('인증 프로그램 입니다.')
id = input('ID를 입력하세요 : ')

if id in save_id :
    pw = int(input('비밀번호를 입력하세요 : '))
    if pw == save_pw[id] :
        print('환영합니다')
    else :
        print('비밀번호를 확인하세요')
else :
    print('ID를 확인하세요')


# if save_id.index(id) = True :