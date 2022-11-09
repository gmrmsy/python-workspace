flt = 123.123
print( "round(flt,0) : ",round(flt,0))
print( "round(flt,1) : ",round(flt,1))
print( "round(flt,2) : ",round(flt,2))
print("\n")

py = 70
c = 50
ja= 75
sum_ = py+c+ja
print('합 :',sum_)
print('평균 :',round(sum_/3,2))
print("\n")

num = 11
minute = 37
print('평균 시간 :',round(minute/num,2))
print("\n")

oneF = 500.23
avgF = 260
print('총 높이 :',round((oneF+avgF*13)/100,3))
print("\n")

flt = 123.123
print(flt+20)
print("\n")

st = '파' ; st1 = '이썬'
print(st+st1)
print("\n")

# type()  어떤 타입의 자료인지 확인
print(type(st))  #  str  문자열
print(type(flt))  #  float  실수값
print(type(num))  # int  정수값
print("\n")

# 형변환
print(type(str(num)))
print(type(num))
print(st+str(num))
print("\n")

su = 100
num = "100"
flt = "1.111"
print(su+int(num))
print(su+float(flt))
print(int(num)+float(flt))
print(str(su)+num)
print(int(float(flt)))  # 문자열->실수값->정수값 / 실수값->정수값일때는 소수점을 버린다.
print("\n")
'''
num = input('숫자 입력 : ')
print('입력 받은 수 : ',num)
print("\n")
''''''
name = input('이름 입력 : ')
age = input('나이 입력 : ')
print('=> 결과 출력 : {} 님의 나이는 {} 살 입니다.'.format(name,age))
print("\n")
''''''
print('두 수의 합을 구해줍니다.')
n1 = input('수 입력 : ')
n2 = input('수 입력 : ')
n3 = n1 + n2
print('두 수의 합 : ',n3)
print("\n")

print('두 수의 합을 구해줍니다.')
n1 = int(input('수 입력 : '))
n2 = int(input('수 입력 : '))
n3 = n1 + n2
print('두 수의 합 : ',n3)
print("\n")

print('두 수의 합을 구해줍니다.')
n1 = input('수 입력 : ')
n2 = input('수 입력 : ')
n3 = int(n1) + int(n2)
print('두 수의 합 : ',n3)
print("\n")
''''''
pre = int(input('올해 년도 4자리를 입력하세요 : '))
birth = int(input('당신이 태어난 년도 4자리를 입력하세요 : '))
print('당신의 나이는 {}살 입니다.'.format(pre-birth+1))
print("\n")

st = float(input('첫 번째 물건의 무게를 입력하시오 : '))
nd = float(input('첫 번째 물건의 무게를 입력하시오 : '))
print ('현재 엘리베이터의 허용 무게는 {}kg 입니다.'.format(600-st-nd))
''''''
st = float(input('첫 번째 물건의 무게를 입력하시오 : '))
nd = float(input('두 번째 물건의 무게를 입력하시오 : '))
if st+nd<600 :
    print ('현재 엘리베이터의 허용 무게는 {}kg 입니다.'.format(600-st-nd))
else :
    print('허용 무게를 초과하였습니다.')
print("\n")
''''''
height = float(input('키를 입력하세요'))
weight = float(input('현재 체중을 입력하세요.'))
heightD = (height-100)*0.9
weightD = weight/heightD*100

print('표준 체중은 {}kg 이고 비만도는 {}입니다.'.format(heightD,weightD))
print("\n")
''''''
name = input('학생 이름 : ')
K = int(input('국어 점수 : '))
E = int(input('영어 점수 : '))
M = int(input('수학 점수 : '))
sum_ = K+E+M
avg = sum_/3

print('{:=^42}'.format('학생 정보'))
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*45)
print('{}\t{}\t{}\t{}\t{}\t{}'.format(name,K,E,M,sum_,round(avg,2)))
print("\n")

if avg>80 :
    print('참 잘했어요')
else :
    print('공부하자')
print("\n")
'''
