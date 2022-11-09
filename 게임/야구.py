import random
import math
import time

num_m = 940124

while num_m != 3 :
    print('□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
    print('□□□□□□■□□□■■■■□□■■■■□■□■□□■■□□■□')
    print('□□■■□□■■□□□□□■□□□□□■□■□■□■□□■□■□')
    print('□■□□■□■□□□□□□■□□□□■□■■□■□■□□■□■□')
    print('□■□□■□■■□■■■■■■□□■□□□■□■□□■■□□■□')
    print('□□■■□□■□□□□□■□□□■□□□□■□■□□□■■■■□')
    print('□□□□□□■□□□□□■□□□□□□□□■□■□□□■□□■□')
    print('□□□□□□□□□□□□□□□□□□□□□□□□□□□■■■■□')
    print('□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
    print('\n')
    print('1. 게임선택')
    print('2. 게임설명')
    print('3. 게임종료')
    num_m = int(input('메뉴선택 : '))
    

    if num_m == 1 :
        num = 940124
        while num != 5 :
            print('\n')
            print('\n')
            print('1. 2자리수')
            print('2. 3자리수')
            print('3. 4자리수')
            print('4. 5자리수')
            print('5. 이전 단계로')
            num = int(input('난이도 선택 : '))
            num_1 = 0
        
            if num == 1 :
                start = time.time()
                print('\n')
                print('\n')
                print('2자리수 게임이 실행 됩니다.') 
                ran = random.randint(10,99)
                player = 0
                while ran != player :
                    num_1 += 1
                    player = int(input('예상숫자를 적으시오 : '))
                    while player < 10 :
                        player = int(input('2자리 숫자를 적으세요 :'))
                    while player > 99 :
                        player = int(input('2자리 숫자를 적으세요 :'))
                    ran10 = ran//10
                    ran1 = ran-(ran10*10)
                    player10 = player//10
                    player1 = player-(player10*10)
                    Bcount = 0
                    Scount = 0
                    
                    if ran10 == player10 :
                        Scount += 1
                    else :
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player10 :
                                Bcount += 1

                    if ran1 == player1 :
                        Scount += 1
                    else :
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player1 :
                                Bcount += 1
                                
                    print(f'{Bcount}B {Scount}S')
                end = time.time()
                time_rec = end - start
                print('\n')
                print('{}회 만에 정답!'.format(num_1))
                print('소요시간 : {}초'.format(round(time_rec,2)))
                print('\n')
                print('\n')
            
            if num == 2 :
                start = time.time()
                print('\n')
                print('\n')
                print('3자리수 게임이 실행 됩니다.') 
                ran = random.randint(100,999)
                player = 0
                while ran != player :
                    num_1 += 1
                    player = int(input('예상숫자를 적으시오 :'))
                    while player < 100 :
                        player = int(input('3자리 숫자를 적으세요 :'))
                    while player > 999 :
                        player = int(input('3자리 숫자를 적으세요 :'))
                    ran100 = ran//100
                    ran10 = (ran-(ran100*100))//10
                    ran1 = ran-(ran10*10)-(ran100*100)
                    player100 = player//100
                    player10 = (player-(player100*100))//10
                    player1 = player-(player10*10)-(player100*100)
                    Bcount = 0
                    Scount = 0
                    
                    if ran100 == player100 :
                        Scount += 1
                    else :
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player100 :
                                Bcount += 1                            
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player100 :
                                Bcount += 1
                    
                    
                    if ran10 == player10 :
                        Scount += 1
                    else :
                        if ran100 == player100 :
                            pass
                        elif ran100 != player100 :
                            if ran100 == player10 :
                                Bcount += 1                            
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player10 :
                                Bcount += 1

                    if ran1 == player1 :
                        Scount += 1
                    else :
                        if ran100 == player100 :
                            pass
                        elif ran100 != player100 :
                            if ran100 == player1 :
                                Bcount += 1                            
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player1 :
                                Bcount += 1                            

                    print(f'{Bcount}B {Scount}S')
                end = time.time()
                time_rec = end - start
                print('\n')
                print('{}회 만에 정답!'.format(num_1))
                print('소요시간 : {}초'.format(round(time_rec,2)))
                print('\n')
                print('\n')
            
            if num == 3 :
                start = time.time()
                print('\n')
                print('\n')
                print('4자리수 게임이 실행 됩니다.') 
                ran = random.randint(1000,9999)
                player = 0
                while ran != player :
                    num_1 += 1
                    player = int(input('예상숫자를 적으시오 : '))
                    while player < 1000 :
                        player = int(input('4자리 숫자를 적으세요 :'))
                    while player > 9999 :
                        player = int(input('4자리 숫자를 적으세요 :'))
                    ran1000 = ran//1000
                    ran100 = (ran-(ran1000*1000))//100
                    ran10 = (ran-(ran100*100)-(ran1000*1000))//10
                    ran1 = ran-(ran10*10)-(ran100*100)-(ran1000*1000)
                    player1000 = player//1000
                    player100 = (player-(player1000*1000))//100
                    player10 = (player-(player100*100)-(player1000*1000))//10
                    player1 = player-(player10*10)-(player100*100)-(player1000*1000)
                    Bcount = 0
                    Scount = 0

                    
                    if ran1000 == player1000 :
                        Scount += 1
                    else :
                        if ran100 == player100 :
                            pass
                        elif ran100 != player100 :
                            if ran100 == player1000 :
                                Bcount += 1                            
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player1000 :
                                Bcount += 1
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player1000 :
                                Bcount += 1

                    if ran100 == player100 :
                        Scount += 1
                    else :
                        if ran1000 == player1000 :
                            pass
                        elif ran1000 != player1000 :
                            if ran1000 == player100 :
                                Bcount += 1                            
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player100 :
                                Bcount += 1
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player100 :
                                Bcount += 1

                    if ran10 == player10 :
                        Scount += 1
                    else :
                        if ran1000 == player1000 :
                            pass
                        elif ran1000 != player1000 :
                            if ran1000 == player10 :
                                Bcount += 1                            
                        if ran100 == player100 :
                            pass
                        elif ran100 != player100 :
                            if ran100 == player10 :
                                Bcount += 1
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player10 :
                                Bcount += 1

                    if ran1 == player1 :
                        Scount += 1
                    else :
                        if ran1000 == player1000 :
                            pass
                        elif ran1000 != player1000 :
                            if ran1000 == player1 :
                                Bcount += 1                            
                        if ran100 == player100 :
                            pass
                        elif ran100 != player100 :
                            if ran100 == player1 :
                                Bcount += 1
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player1 :
                                Bcount += 1
                    
                    print(f'{Bcount}B {Scount}S')
                end = time.time()
                time_rec = end - start
                print('\n')
                print('{}회 만에 정답!'.format(num_1))
                print('소요시간 : {}초'.format(round(time_rec,2)))
                print('\n')
                print('\n')

            if num == 4 :
                start = time.time()
                print('\n')
                print('\n')
                print('5자리수 게임이 실행 됩니다.') 
                ran = random.randint(10000,99999)
                player = 0
                while ran != player :
                    num_1 += 1
                    player = int(input('예상숫자를 적으시오 : '))
                    while player < 10000 :
                        player = int(input('5자리 숫자를 적으세요 :'))
                    while player > 99999 :
                        player = int(input('5자리 숫자를 적으세요 :'))
                    ran10000 = ran//10000
                    ran1000 = (ran-(ran10000*10000))//1000
                    ran100 = (ran-(ran1000*1000)-(ran10000*10000))//100
                    ran10 = (ran-(ran100*100)-(ran1000*1000)-(ran10000*10000))//10
                    ran1 = ran-(ran10*10)-(ran100*100)-(ran1000*1000)-(ran10000*10000)
                    player10000 = player//10000
                    player1000 = (player-(player10000*10000))//1000
                    player100 = (player-(player1000*1000)-(player10000*10000))//100
                    player10 = (player-(player100*100)-(player1000*1000)-(player10000*10000))//10
                    player1 = player-(player10*10)-(player100*100)-(player1000*1000)-(player10000*10000)
                    Bcount = 0
                    Scount = 0

                    if ran10000 == player10000 :
                        Scount += 1
                    else :
                        if ran1000 == player1000 :
                            pass
                        elif ran1000 != player1000 :
                            if ran1000 == player10000 :
                                Bcount += 1
                        if ran100 == player100 :
                            pass
                        elif ran100 != player100 :
                            if ran100 == player10000 :
                                Bcount += 1                            
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player10000 :
                                Bcount += 1
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player10000 :
                                Bcount += 1

                    if ran1000 == player1000 :
                        Scount += 1
                    else :
                        if ran10000 == player10000 :
                            pass
                        elif ran10000 != player10000 :
                            if ran10000 == player1000 :
                                Bcount += 1
                        if ran100 == player100 :
                            pass
                        elif ran100 != player100 :
                            if ran100 == player1000 :
                                Bcount += 1                            
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player1000 :
                                Bcount += 1
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player1000 :
                                Bcount += 1

                    if ran100 == player100 :
                        Scount += 1
                    else :
                        if ran10000 == player10000 :
                            pass
                        elif ran10000 != player10000 :
                            if ran10000 == player100 :
                                Bcount += 1
                        if ran1000 == player1000 :
                            pass
                        elif ran1000 != player1000 :
                            if ran1000 == player100 :
                                Bcount += 1                            
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player100 :
                                Bcount += 1
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player100 :
                                Bcount += 1

                    if ran10 == player10 :
                        Scount += 1
                    else :
                        if ran10000 == player10000 :
                            pass
                        elif ran10000 != player10000 :
                            if ran10000 == player10 :
                                Bcount += 1
                        if ran1000 == player1000 :
                            pass
                        elif ran1000 != player1000 :
                            if ran1000 == player10 :
                                Bcount += 1                            
                        if ran100 == player100 :
                            pass
                        elif ran100 != player100 :
                            if ran100 == player10 :
                                Bcount += 1
                        if ran1 == player1 :
                            pass
                        elif ran1 != player1 :
                            if ran1 == player10 :
                                Bcount += 1

                    if ran1 == player1 :
                        Scount += 1
                    else :
                        if ran10000 == player10000 :
                            pass
                        elif ran10000 != player10000 :
                            if ran10000 == player1 :
                                Bcount += 1
                        if ran1000 == player1000 :
                            pass
                        elif ran1000 != player1000 :
                            if ran1000 == player1 :
                                Bcount += 1                            
                        if ran100 == player100 :
                            pass
                        elif ran100 != player100 :
                            if ran100 == player1 :
                                Bcount += 1
                        if ran10 == player10 :
                            pass
                        elif ran10 != player10 :
                            if ran10 == player1 :
                                Bcount += 1
                    
                    print(f'{Bcount}B {Scount}S')
                end = time.time()
                time_rec = end - start
                print('\n')
                print('{}회 만에 정답!'.format(num_1))
                print('소요시간 : {}초'.format(round(time_rec,2)))
                print('\n')
                print('\n')
                
            num = 5
            print('\n')
            print('\n')

    if num_m == 2 :
        print('\n')
        print('\n')
        print('========== 게임 설명 ==========')
        print('1. 예상되는 숫자를 입력한다.')
        print('2. 자리수는 틀리되 포함되는 숫자는 1B, \n   자리수까지 맞는 숫자는 1S로 개수를 센다.')
        print('3. 정답숫자를 맞추면 승리')
        print('ex) 정답숫자 : 479')
        print('ex) 예상숫자 : 407')
        print('ex)   결 과  : 1B 1S')
        print('\n')
        print('========== 주 의 ==========')
        print('ex) 정답숫자 : 4449')
        print('    예상숫자 : 4044')
        print('    결 과  : 1B 2S')
        print('    정답숫자에 중복되는 수가 있을 경우')
        print('    일치하는 예상숫자와 정답숫자는')
        print('    다른 자리 숫자와 중복되서 카운트되지 않는다')
        print('\n')
        print('\n')

