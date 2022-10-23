################################ 1일차 ################################
print( 20 + 200 )
print ("안녕하세여") #문자열일 경우 ""(큰따옴표) 혹은 ''(작은따옴표) 사이에 작성
print ( 100 ) ; print ( 2000 ) # ;(세미클론) 마침표의 의미 이거 안쓰면 문장이 계속된다고 인식한다.
# 이거는 포함 안되지롱

# ''는 한줄은 커버가 안된다

'''안녕
하세요'''

# '''     ''' 으로 묶으면 여러줄 커버가능

print("""안
      녕
      하
      세
      요 """)
print("\n")


'''
ESCAPE 문자 - 문자열 안에서 특수한 동작을 해주는 것
                     - \n : 엔터값과 비슷하다
                     - \t : tap크기만큼 커서를 오른쪽으로 이동 (빈칸안에 앞 내용을 채워넣는다, 8자이상이면 다시8칸 추가)
                     - \" : "(큰따옴표) 출력
                     - \' : '(작음따옴표) 출력
'''

print("안\n녕\n하\n세\n요")
print(" Have\ta\t\tgood\ttime")
print("1234567\t1\t12345678\t55")
print("이름\t나이\t성별\t비고")
print("이효재\t29\t남\t파이썬")
print("\n")

print(" '안녕' '''' ")
#print(" "안녕" ")  오류가 생긴다
print(" \"안녕\" ")
print( "C:\\Users\\user\\Documents\\k-디지털" ) # \하나만 사용시 오류가 날 수도 있다
print( "C:\\Users\\user\\Documents\\k-디지털" )
print( "C:/Users/user/Documents/k-디지털" )
print("\n")

print("="*48)
print("\t\t####회비정보####")
print("=="*24)
print("==="*16)
print("이름\t\t나이\t전화번호\t\t회비")
print("===="*12)
print("======"*8)
print("홍길동\t\t\"15\"\t010-123-1234\t|20,000")
print("임꺽정\t\t\"20\"\t010-234-2345\t|30,000")
print("김말이\t\t\"28\"\t010-345-3456\t|50,000")
print("========"*6)
print("============"*4)
print("총합계\t\t\t\t\t|100,000")
print("================"*3)
print("\n")

print("\t\t####회비정보####\n================================================\n이름\t\t나이\t전화번호\t\t회비\n================================================\n홍길동\t\t\"15\"\t010-123-1234\t|20,000\n임꺽정\t\t\"20\"\t010-234-2345\t|30,000\n김말이\t\t\"28\"\t010-345-3456\t|50,000\n================================================\n총합계\t\t\t\t\t|100,000")
print("\n")

print(1+2+3+4+6)
print(6-4-3-2-1)
print(1*2*3*4*6)
print(6/4/3/2/1)
print(' 안녕' , 123+123)  #문자열, 숫자열 서로다른 문장을 넣을때는 ,(콤마)로 구분
print('100') #보기에는 숫자열이지만 문자열로 읽힌다
print('100'+'100')
print("안녕"+"디지몬")
print("\n")


print("12 + 54 =",12 + 54,"입니다")
print("268 - 48 =",268 - 48,"입니다")
print("2 * 23 =",2*23,"입니다")
print("120 / 3 =",120/3,"입니다")
print("\n")

print(f"12+54= {12+54} 입니다")  # f 문자열 안에 숫자열작성
print(f"268 - 48 = {268 - 48} 입니다")
print(f"2 * 23 = {2 * 23} 입니다")
print(f"120 / 3 = {120 / 3} 입니다")
print("\n")

print("12+54= {} 입니다".format(12+54))
print("{}+{}= {} 입니다".format(10,20,30))
print("{2}+{1}= {0} 입니다".format(10,20,30))
print("\n")

print("{:,}".format(10000000000000))
print("{:<10}왼쪽정렬{:<10}".format('안녕','하세'))
print("{:<10}왼쪽정렬{:0<10}".format('안녕','하세'))
print("{:>10}오른쪽정렬{:>10}".format('안녕','하세'))
print("{:>10}오른쪽정렬{:8>10}".format('안녕','하세'))
print("{:^10}가운데정렬{:^10}".format('안녕','하세'))
print("{:^10}가운데정렬{:6^10}".format('안녕','하세'))
print("\n")


'''
변수
- 데이터를 저장하기 위한 공간
- 데이터는 언제든지 변경 가능하다
- 의미를 부여해서 만든다
- 키워드(예약어)는 사용할 수 없다 ex)print, format
- 한글로 이름할 수 있으나 영어로 만드는 것이 좋다
'''

# =  대입 연산자 / 오른쪽에 있는 결과값을 왼쪽에 저장한다
num = 1000
print("저장값",num,"입니다")
print(f"저장값 {num}입니다")
print("저장값{}입니다".format(num))

num = 5
print( '변경후',num)   # 뒤에 같은 이름으로 설정하면 갱신된다

num = num + 100
print('연산 후 :',num)   # 대입 연산자는 오른쪽에 있는 결과값을 왼쪽에 저장하는거기 때문에 오른쪽num은 5가 들어가지 않는다

num1 = 5
num2 = 10
Sum = num1+num2
print('n1 :',num1)
print('n2 :',num2)
print('sum:',Sum)


num1 = 10
num2 = 20
print("{:-^20}".format(" 출력 결과 "))
print("num1({}) + num2({}) = {}".format(num1,num2,num1+num2))
print("\n")

num1 = 10
num2 = 20
print("{:-^20}".format(" 출력 결과 "))
print(f"num1({num1}) + num2({num2}) = {num1+num2}")
print("\n")

################################ 2일차 ################################

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
################################ 3일차 ################################
'''
연산자 \ + 는 더하기 \ - 는 빼기 \ * 는 곱하기 \ / 는 나누기 \ % 는 나머지 \ // 는 몫 \ ** 는 거듭제곱
'''
'''
비교연산자
== 값이 동일하다
!= 값이 동일하지 않다
> 왼쪽 값이 오른쪽 값보다 크다
< 왼쪽 값이 오른쪽 값보다 작다
>= 왼쪽 값이 오른쪽 값보다 크거나 같다
<= 왼쪽 값이 오른쪽 값보다 작거나 같다
'''
'''
복합대입연산자
+= , -= , *=
a = 10 ; => a=a+100 => a+=100
'''
su1 = su2 = 5
su1 += 1 ; print('su1 += 1 => ',su1)
su1 -= 1 ; print('su1 -= 1 => ',su1)
su1 *= su2 ; print('su1 *= su2 => ',su1)
su1 //= su2 ; print('su1 //= su2 => ',su1)
su1 %= su2 ; print('su1 %= su2 => ',su1)
print('\n')

su1 = 5 ; su2 = 3 ;
su1 **= su2
su1 -= 2
print('su1 / 4  : ',su1 / 4)
print('su1 // 4  : ',su1 // 4)
print('su1 % 4  : ',su1 % 4)
print('\n')

'''
논리연산자
참 또는 거짓을 표현
and , or , not
or (값or값) : 하나라도 참이면 결과는 참
and (값 and값) : 하나라도 거짓이면 결과는 거짓
         모두 참일 때 참
not (not값) : 결과 값을 반전시켜준다
'''

print( False or False )
print( (10>20) or (10%2 == 0) )
print( False and True )
print(True and True )
print( (10>20) and (10%2 == 0) )

# 짝수 홀수 구분 : 2로 나누어 나머지값이 0이면 짝수 1이면 홀
a = 100
print( a>10 and a%2==0 )

print( not True )
print( not False )
print('\n')

print('1.쉬운게임')
print('2.어려게임')
print('3.게임종료')
# num = int(input('>>>>> : '))
num = 1
if num == 1 :
    print('쉬운 게임이 실행 됩니다.') ;
if num == 2 :
    print('어려운 게임이 실행 됩니다.')
if num == 3 :
    print('게임을 종료합니다.')
print('다음 문장')
print('\n')

num1 = 10 ; num2 = 15
if num1 > num2 :
    print('참인경우 실행')
print('다음문장')
print('\n')

num = int(input('숫자를 입력하세요 : '))
if num % 3 == 0 :
    print('3의 배수입니다.')
if num % 3 != 0 :
    print('3의 배수가 아닙니다.')
print('\n')

num = int(input('숫자를 입력하세요 : '))
if num % 2 ==0 :
    print('짝수 입니다.')
if num % 2 ==1 :
    print('홀수 입니다.')
print('\n')

num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))
if num1 > num2 :
    print(num1)
if num1 < num2 :
    print(num2)
print('\n')

num = int(input('숫자를 입력하세요 : '))
if num >= 0 :
    print(num)
if num < 0 :
    print(num* -1)

num = int(input('날짜를 입력하세요 : '))
if num%7 == 1 :
    print('월요일 입니다.')
if num%7 == 2 :
    print('화요일 입니다.')
if num%7 == 3 :
    print('수요일 입니다.')
if num%7 == 4 :
    print('목요일 입니다.')
if num%7 == 5 :
    print('금요일 입니다.')
if num%7 == 6 :
    print('토요일 입니다.')
if num%7 == 0 :
    print('일요일 입니다.')
print('\n')

num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))
num3 = int(input('세번째 숫자를 입력하세요 : '))
num12 = num1 > num2
num13 = num1 > num3
num23 = num2 > num3
if num12 and num13 :
    print(num1)
if not num12 and num23 :
    print(num2)
if not num13 and not num23 :
    print(num3)
print('\n')

num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))
if num1 - num2 < 0 :
    if num2 % 2 == 0 :
        print(num1,num2)
if num2 - num1 < 0 :
    if num1 % 2 == 0 :
        print(num1,num2)
print('\n')

num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))
if (num1+num2) % 2 ==0 and (num1+num2) % 3 == 0 :
    print(num1,num2)

