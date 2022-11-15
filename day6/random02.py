'''
범위를 지정해서 특정 범위의 무작위 수를 뽑는다
'''
import random

for i in range(5):
    print( random.random(), end=" ")
print()
for i in range(5):
    print( int(random.random()*3), end=" ")
'''
0.000 ~ 0.9999 * 3
int(0.000 ~ 2.9999)
    0 ~ 2
'''
print()
for i in range(5):
    print( random.randrange(0,3), end=" ")
print("======")
# 로또프로그램 생성
# 1~45 사이의 무작위 중복되지 않는 6개의 수
ls = []
while len(ls) < 6:
    num = random.randrange(1,46)
    if ls.count( num ) == 0:
        ls.append( num )
ls.sort()
print( ls )

s = set()
while True:
    s.add( random.randrange(1,7) )
    if len(s) == 6:
        break
print( s )

import  random
best = 100 
while True:
    cnt = 0
    print("1.게임시작 2.최고기록 확인 3.종료" )
    num = int( input(">>> : ") )
    if num == 1:
        com = random.randrange( 1, 100 )
        print("com : ",com)
        while True:
            cnt += 1;  user = int( input("수 입력 : " ) )
            if user == com:
                print("정답")
                if(cnt < best):
                    print("최고기록 갱신" );  best = cnt
                break
            elif user > com:  print("down" )
            else:  print("up" )
    elif num == 2:
        if best == 100:  print("게임 먼저 진행하세요" )
        else:  print("최고 기록 : ", best )
    elif num == 3:  print("게임 종료" );  break



import  random
best = 100
while True:
    cnt = 0
    print("1.게임시작 2.최고기록 확인 3.종료" )
    num = int( input(">>> : ") )
    if num == 1:
        cnt = 0
        com_set = set()
        while True:
            com_set.add( random.randrange( 1, 10 ) )
            if len( com_set ) == 3: break
        com = list( com_set )
        print("com : ",com)
        # com = [ 3, 5, 9]
        result = [ 0, 0, 0 ]#스트라잌, 볼, 아웃
        while True:
            cnt += 1;
            for i in range(3):
                input_user = int( input("수 입력 : " ) )
                if input_user == com[i]:  result[0] += 1
                elif com.count( input_user ) != 0:
                    result[1] += 1
                else:  result[2] += 1
            print(f"{result[0]}스트라이크, {result[1]}볼, {result[2]}아웃")
            if result[0] == 3:
                break
            result = [ 0, 0, 0 ]
        if cnt < best: print(cnt,"회. 최고 기록 갱신" );  best = cnt
        else:  print(cnt,"회만에 맞추셨습니다" )
               
    elif num == 2:
        if best == 100:  print("게임 먼저 진행하세요" )
        else:  print("최고 기록 : ", best )
    elif num == 3:  print("게임 종료" );  break










    




