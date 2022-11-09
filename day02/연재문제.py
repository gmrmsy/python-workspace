print('{:=^20}'.format('성적 입력창'))
print(':b 점수는 0 ~ 100 사이 입력! d:')
print("'ㅁ' 아니면 처음부터 다시! 'ㅁ'")
print()

name = input('학생 이름 : ')

K = 0 ; E = 0 ; M = 0

K = int(input('국어 점수 : '))
E = int(input('영어 점수 : '))
M = int(input('수학 점수 : '))

if K < 0 or K > 100 or E < 0 or E > 100 or M < 0 or M > 100 :
    if K < 0 or K > 100 :
        print('국어점수를 다시 입력하세요')    
    if E < 0 or E > 100 :
        print('영어점수를 다시 입력하세요')
    if M < 0 or M > 100 :
        print('수학점수를 다시 입력하세요')    
else :
    sum_ = K+E+M
    avg = sum_ / 3

    if avg >= 90 :
        score = 'A'
    elif avg >= 80 :
        score = 'B'
    elif avg >= 70 :
        score = 'C'
    else :
        score = 'D'
    print('{:=^20}'.format('성적 출력창'))
    print('이름\t학점')
    print(f'{name}\t{score}')