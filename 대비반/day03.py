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

