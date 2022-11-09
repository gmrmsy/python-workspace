'''
import os  # 원도우 명령어 사용
os.system('pause')  # 일시정지
os.system('cls')  # 출력창 지우기

######

#import sys, os
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

#import day2.elif05
#print("현재페이지")
'''
import os

#data = 0;
data = None


while True:
    print("="*30)
    print("1.데이터 입력")
    print("2.데이터 출력")
    print("3.종료")
    print("="*30)
    num = int(input(">>> : "))
    if num == 1:
        data = input("데이터 입력 => ")
    elif num == 2:
        if data == None:
            print("저장 데이터 없음")
        else:
            print("입력 데이터 : ",data)
        os.system("pause")
    elif num == 3:
        os._exit(1)
    os.system("cls")    


'''
num = 0

while num != 6 :
    print('='*30)
    print('{: ^30}'.format('MENU'))
    print('='*30)
    print('1. 학생 이름 입력')
    print('2. 성적 3과목(국, 영, 수) 입력')
    print('3. 학생 이름 출력')
    print('4. 합계 출력')
    print('5. 평균 출력')
    print('6. 종료')
    num = int(input('메뉴를 선택하세요 : '))
    print()

    if num == 1 :
        name = input('학생 이름을 입력하세요 : ')
        print()
    if num == 2 :
        K = int(input('국어성적을 입력하세요 : '))
        E = int(input('영어성적을 입력하세요 : '))
        M = int(input('수학성적을 입력하세요 : '))
        print()
    if num == 3 :
        print(f'학생이름은 {name}입니다')
        print()
    if num == 4 :
        print(f'성적 합계는 {K+E+M}점 입니다.')
        print()
    if num == 5 :
        print(f'평균 점수는 {(K+E+M)/3}점 입니다.')
        print()



st = 'It is a fun Python class'
a_ = 0
s_ = 0
n_ = 0

for i in st :
    if i == 'a' :
        a_ += 1
    if i == 's' :
        s_ += 1
    n_ += 1
print('===결과===')
print(a_)
print(s_)
print(n_)'''