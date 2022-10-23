'''
if 조건식:
    종속문장
else:
    종속문장
다음문장
'''
'''
num = int(input('수 입력 : '))
num = 1
if num == 1:
    print('1입력')
else:
    print('그 외의 값 입력')
print("다음 문장들 실행")

save_id = input('저장할 id 입력 : ')
save_id='aaa'
print('인증 프로그램')
#input_id = input('비교할 id 입력 : ')
input_id='aaa'
if save_id == input_id:
    print('인증 통과')
else:
    print('인증 실패')

num = 9
if num % 3 == 0:
    if num % 2 == 0:
        print("num 2,3의 배수 입니다.")
        print("num 짝수이며 3의 배수 입니다")
    else:
        print('num 3의 배수이며 짝수는 아니다')
else:
    print('num은 3의 배수가 아닙니다')
print("다음 문장들 실행")
'''
'''
user = int(input('GByte 입력 : '))
select = int(input('1.byte 2. Kbyte 3. Mbyte >>>>  '))

if select == 3 :
    print('{}GB : {} Mbyte'.format(user,user*1024))
if select == 2 :
    print('{}GB : {} Kbyte'.format(user,user*1024*1024))
if select == 1 :
    print('{}GB : {} byte'.format(user,user*1024*1024*1024))
'''

'''
save_ID = input('저장할 ID 입력 : ')
save_PW = input('저장할 PW 입력 : ')
input_ID = input(('ID 입력 : '))
input_PW = input(('PW 입력 : '))

if save_ID == input_ID :
    pass
else :
    print('해당 아이디는 없습니다')
if save_PW == input_PW :
    print('인증완료')
else :
    print('비밀번호가 틀렸습니다.')
'''

'''
if 조건식 :  /  if문이 참이면 종속문장 진행, 거짓일 경우 elif진행, 후속문장에 참이 없을 경우 elif 진행
    종속문장
elif 조건식 :
    종속문장
elif ,,,,,,,,,, :

else :
    종속문장
'''
'''
num = int(input('수 입력 : '))
if num > 100 :
    print('100보다 크다')
elif num > 50 :
    print('50보다 크다')
elif num > 0 :
    print('0보다 크다')
else :
    print('그 외의 값 입력')
print('다음 문장들 실행')
'''
'''
num = int(input('수 입력 : '))
if num > 100 :
    print('100보다 크다')
if num > 50 :
    print('50보다 크다')
if num > 0 :
    print('0보다 크다')
else :
    print('그 외의 값 입력')
print('다음 문장들 실행')
'''
'''
nume = input('이름을 입력하시오 : ')
ID = input('학번을 입력하시오 : ')
sub1 = int(input('1번과목 점수 : '))
sub2 = int(input('2번과목 점수 : '))
sub3 = int(input('3번과목 점수 : '))

if (sub1+sub2+sub3)/3 > 90 :
    print('성적 : A')
elif (sub1+sub2+sub3)/3 > 80 :
    print('성적 : B')
elif (sub1+sub2+sub3)/3 > 70 :
    print('성적 : C')
elif (sub1+sub2+sub3)/3 > 60 :
    print('성적 : D')
else :
    print('성적 : F')
'''
'''
coffee = int(input('몇 잔? : '))
if coffee > 10 :
    print('{}원 입니다.'.format((coffee-10)*1500+20000))
else :
    print('{}원 입니다.'.format(coffee*2000))
'''
'''
num = int(input('정수를 입력하세요 : '))
if num == 0 :
    print('0은 3의 배수도, 4의 배수도 아닙니다.')
elif num%3 == 0 :
    if num%4 == 0 :
        print('3의 배수이면서, 4의 배수입니다.')
    elif num%4 != 0 :
        print('3의 배수입니다.')
elif num%3 != 0 :
    if num%4 == 0 :
        print('4의 배수입니다.')
    elif num%3 != 0 :
        print('3의 배수도, 4의 배수도 아닙니다.')
'''
'''
time = int(input('비행시간을 입력하세요 (분) : '))
if time > 30 :
    if time%10 != 0 :
        print('총 요금은 {}원 입니다.'.format(30000+(((time-30)//10)+1)*5000))
    elif time%10 == 0 :
        print('총 요금은 {}원 입니다.'.format(30000+(((time-30)//10))*5000))
else :
    print('총 요금은 30,000원 입니다.')
'''
'''
while True :  # 조건이 참이면 계속 반복한다. / 강제종료는 Ctrl+C
    print('='*20)
    print('1. 데이터 입력')
    print('2. 데이터 출력')
    print('3. 종료')
    print('='*20)
    num = int(input('>>> : '))
    if num ==1 :
        data = input('데이터 입력 ; ')
    elif num ==2 :
        print('입력데이터 :',data)
    else :
        print('종료합니다.')
        break
'''
'''
num = 940124
while num !=6 :
    print('='*40)
    print('{:^40}'.format('M E N U'))
    print('='*40)
    print('1. 학생 이름 입력')
    print('2. 성적 3과목 (국, 영. 수) 입력')
    print('3. 학생 이름 출력')
    print('4. 합계 출력')
    print('5. 평균 출력')
    print('6. 종료')
    print('='*40)
    num = int(input('선택 : '))
    if num == 1 :
        name = input('이름을 입력하세요. : ')
    elif num == 2  :
        K = int(input('국어 성적을 입력하세요. : '))
        E = int(input('영어 성적을 입력하세요. : '))
        M = int(input('수학 성적을 입력하세요. : '))
    elif num == 3 :
        print(name)
    elif num == 4 :
        print('{}점'.format(K+E+M))
    elif num ==5 :
        print('{}점'.format((K+E+M)/3))
'''
import math
import time

start = time.time()
# math.factorial(100000)
input('asoivjwp')
end = time.time()

time = end - start



print('소요시간 : {}초'.format(round(time,2)))
