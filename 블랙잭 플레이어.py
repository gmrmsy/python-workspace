import random

### 덱 생성 ###
pat = ['♥', '◆', '♣', '♠']
num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []

for i in pat :
    for k in num :
        deck.append(f'{i}'+f'{k}')
############

### 기본 카드 ###
player = []
for i in  range(1, 3, 1) :
    pick = f'{random.choice(deck)}'
    locals()['p1_p'+str(i)]= pick[:1]
    locals()['p1_n'+str(i)] = pick[1:]
    locals()['p1_c'+str(i)] = locals()['p1_p'+str(i)]+locals()['p1_n'+str(i)]
    player.append(locals()['p1_c'+str(i)])
    deck = list(set(deck)-set(player))

cpu = []
for i in  range(1, 3, 1) :
    pick = f'{random.choice(deck)}'
    locals()['c1_p'+str(i)]= pick[:1]
    locals()['c1_n'+str(i)] = pick[1:]
    locals()['c1_c'+str(i)] = locals()['c1_p'+str(i)]+locals()['c1_n'+str(i)]
    cpu.append(locals()['c1_c'+str(i)])
    deck = list(set(deck)-set(cpu))
##############

### 카드 연산 ###
for i in range(1, len(player)+1, 1) :
    if globals()['p1_n'+str(i)] == 'A' :
        globals()['p1_n'+str(i)] = 1
    elif globals()['p1_n'+str(i)] == 'J' :
        globals()['p1_n'+str(i)] = 10
    elif globals()['p1_n'+str(i)] == 'Q' :
        globals()['p1_n'+str(i)] = 10
    elif globals()['p1_n'+str(i)] == 'K' :
        globals()['p1_n'+str(i)] = 10
    else :
        pass

for i in range(1, len(cpu)+1, 1) :
    if globals()['c1_n'+str(i)] == 'A' :
        globals()['c1_n'+str(i)] = 1
    elif globals()['c1_n'+str(i)] == 'J' :
        globals()['c1_n'+str(i)] = 10
    elif globals()['c1_n'+str(i)] == 'Q' :
        globals()['c1_n'+str(i)] = 10
    elif globals()['c1_n'+str(i)] == 'K' :
        globals()['c1_n'+str(i)] = 10
    else :
        pass
#################


game = 0
p_money = 10000
c_money = 10000
g_switch = 1

while p_money > 0 and c_money > 0 :
    b_money = 100000
    print(f'Player : {p_money}$')
    print(f'C P U : {c_money}$')
    while b_money > 1000 :
        b_money = int(input('베팅 금액을 입력하세요 : ')) 
        if b_money > 1000 :
            print('1000$ 이하로 베팅하세요')

    ### 덱 초기화 ###
    pat = ['♥', '◆', '♣', '♠']
    num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []

    for i in pat :
        for k in num :
            deck.append(f'{i}'+f'{k}')
    ################

    ### 기본 카드 ###
    player = []
    for i in  range(1, 3, 1) :
        pick = f'{random.choice(deck)}'
        globals()['p1_p'+str(i)] = pick[:1]
        globals()['p1_n'+str(i)] = pick[1:]
        globals()['p1_c'+str(i)] = globals()['p1_p'+str(i)]+globals()['p1_n'+str(i)]
        player.append(globals()['p1_c'+str(i)])
        deck = list(set(deck)-set(player))

    cpu = []
    for i in  range(1, 3, 1) :
        pick = f'{random.choice(deck)}'
        globals()['c1_p'+str(i)] = pick[:1]
        globals()['c1_n'+str(i)] = pick[1:]
        globals()['c1_c'+str(i)] = globals()['c1_p'+str(i)]+globals()['c1_n'+str(i)]
        cpu.append(globals()['c1_c'+str(i)])
        deck = list(set(deck)-set(cpu))    
    ################

    ### 알파벳 -> 숫자 ###
    for i in range(1, len(player)+1, 1) :
        if globals()['p1_n'+str(i)] == 'A' :
            globals()['p1_n'+str(i)] = 1
        elif globals()['p1_n'+str(i)] == 'J' :
            globals()['p1_n'+str(i)] = 10
        elif globals()['p1_n'+str(i)] == 'Q' :
            globals()['p1_n'+str(i)] = 10
        elif globals()['p1_n'+str(i)] == 'K' :
            globals()['p1_n'+str(i)] = 10
        else :
            pass

    for i in range(1, len(cpu)+1, 1) :
        if globals()['c1_n'+str(i)] == 'A' :
            globals()['c1_n'+str(i)] = 1
        elif globals()['c1_n'+str(i)] == 'J' :
            globals()['c1_n'+str(i)] = 10
        elif globals()['c1_n'+str(i)] == 'Q' :
            globals()['c1_n'+str(i)] = 10
        elif globals()['c1_n'+str(i)] == 'K' :
            globals()['c1_n'+str(i)] = 10
        else :
            pass
    ####################

    p_over = int(p1_n1) + int(p1_n2)
    c_over = int(c1_n1) + int(c1_n2)
    c_possible = 1
    g_switch = 0
    act = 0
    
    while g_switch != 1 :
        print(player)
        print('총 합 :',p_over)
        print('1. Hit   2. Stand')
        act = int(input('행동을 선택하세요 : '))
        print('')
        if act == 1 :
            pick = f'{random.choice(deck)}'
            globals()['p1_p'+str(len(player)+1)] = pick[:1]
            globals()['p1_n'+str(len(player)+1)] = pick[1:]
            globals()['p1_c'+str(len(player)+1)] = globals()['p1_p'+str(len(player)+1)]+globals()['p1_n'+str(len(player)+1)]
            player.append(globals()['p1_c'+str(len(player)+1)])
            deck = list(set(deck)-set(player))

            for i in range(1, len(player)+1, 1) :
                if globals()['p1_n'+str(i)] == 'A' :
                    globals()['p1_n'+str(i)] = 1
                elif globals()['p1_n'+str(i)] == 'J' :
                    globals()['p1_n'+str(i)] = 10
                elif globals()['p1_n'+str(i)] == 'Q' :
                    globals()['p1_n'+str(i)] = 10
                elif globals()['p1_n'+str(i)] == 'K' :
                    globals()['p1_n'+str(i)] = 10
                else :
                    pass
            p_over += int(globals()['p1_n'+str(len(player))])

            if p_over > 21 :
                print(f'\n{player}')
                print('총 합 :',p_over)
                print('Player BUST!')
                p_money -= b_money
                c_money += b_money
                g_switch = 1
            print('\n')

            if c_possible == 1 :
                if c_over < 17 :
                    pick = f'{random.choice(deck)}'
                    globals()['c1_p'+str((len(cpu))+1)] = pick[:1]
                    globals()['c1_n'+str((len(cpu))+1)] = pick[1:]
                    globals()['c1_c'+str((len(cpu))+1)] = globals()['c1_p'+str((len(cpu))+1)]+globals()['c1_n'+str((len(cpu))+1)]
                    cpu.append(globals()['c1_c'+str((len(cpu))+1)])
                    deck = list(set(deck)-set(cpu))
                    
                    for i in range(1, len(cpu)+1, 1) :
                        if globals()['p1_n'+str(i)] == 'A' :
                            globals()['p1_n'+str(i)] = 1
                        elif globals()['p1_n'+str(i)] == 'J' :
                            globals()['p1_n'+str(i)] = 10
                        elif globals()['p1_n'+str(i)] == 'Q' :
                            globals()['p1_n'+str(i)] = 10
                        elif globals()['p1_n'+str(i)] == 'K' :
                            globals()['p1_n'+str(i)] = 10
                        else :
                            pass
                    c_over += int(globals()['p1_n'+str(len(cpu))])

                elif c_over == 21 :
                    c_possible = 2

                elif c_over > 21 :
                    print(f'\n{player}')
                    print('총 합 :',c_over)
                    print('CPU BUST!')
                    p_money += b_money
                    c_money -= b_money
                    g_switch = 1
            
                elif c_over > 16 :
                    stay = []
                    for i in range(1, int(4**(1.8*(c_over-13)))) :
                        stay.append(i)
                    stay_num = random.choice(stay)
                    if stay_num < 4 :
                        globals()['c1_p'+str((len(cpu))+1)] = pick[:1]
                        globals()['c1_n'+str((len(cpu))+1)] = pick[1:]
                        globals()['c1_c'+str((len(cpu))+1)] = globals()['c1_p'+str((len(cpu))+1)]+globals()['c1_n'+str((len(cpu))+1)]
                        cpu.append(globals()['c1_c'+ str((len(cpu))+1)])
                        deck = list(set(deck)-set(cpu))
                        for i in range(1, len(cpu)+1, 1) :
                            if globals()['p1_n'+str(i)] == 'A' :
                                globals()['p1_n'+str(i)] = 1
                            elif globals()['p1_n'+str(i)] == 'J' :
                                globals()['p1_n'+str(i)] = 10
                            elif globals()['p1_n'+str(i)] == 'Q' :
                                globals()['p1_n'+str(i)] = 10
                            elif globals()['p1_n'+str(i)] == 'K' :
                                globals()['p1_n'+str(i)] = 10
                            else :
                                pass
                        c_over += int(globals()['p1_n'+str(len(cpu))])
                        c_possible = 1
                    elif stay_num > 3 :
                        c_possible = 2

        elif act == 2 :
            while c_possible == 1 :
                if c_over < 17 :
                    pick = f'{random.choice(deck)}'
                    globals()['c1_p'+str((len(cpu))+1)] = pick[:1]
                    globals()['c1_n'+str((len(cpu))+1)] = pick[1:]
                    globals()['c1_c'+str((len(cpu))+1)] = globals()['c1_p'+str((len(cpu))+1)]+globals()['c1_n'+str((len(cpu))+1)]
                    cpu.append(globals()['c1_c'+str((len(cpu))+1)])
                    deck = list(set(deck)-set(cpu))
                    
                    for i in range(1, len(cpu)+1, 1) :
                        if globals()['c1_n'+str(i)] == 'A' :
                            globals()['c1_n'+str(i)] = 1
                        elif globals()['c1_n'+str(i)] == 'J' :
                            globals()['c1_n'+str(i)] = 10
                        elif globals()['c1_n'+str(i)] == 'Q' :
                            globals()['c1_n'+str(i)] = 10
                        elif globals()['c1_n'+str(i)] == 'K' :
                            globals()['c1_n'+str(i)] = 10
                        else :
                            pass
                    c_over += int(globals()['c1_n'+str(len(cpu))])

                elif c_over > 21 :
                    print(f'\n{cpu}')
                    print('총 합 :',c_over)
                    print('CPU BUST!')
                    g_switch = 1                   
                    c_possible = 2

                elif c_over == 21 :
                    c_possible = 2
            
                elif c_over > 16 :
                    stay = []
                    for i in range(1, int(4**(1.8*(c_over-13)))) :
                        stay.append(i)
                    stay_num = random.choice(stay)
                    if stay_num < 4 :
                        globals()['c1_p'+str((len(cpu))+1)] = pick[:1]
                        globals()['c1_n'+str((len(cpu))+1)] = pick[1:]
                        globals()['c1_c'+str((len(cpu))+1)] = globals()['c1_p'+str((len(cpu))+1)]+globals()['c1_n'+str((len(cpu))+1)]
                        cpu.append(globals()['c1_c'+ str((len(cpu))+1)])
                        deck = list(set(deck)-set(cpu))
                        for i in range(1, len(cpu)+1, 1) :
                            if globals()['p1_n'+str(i)] == 'A' :
                                globals()['p1_n'+str(i)] = 1
                            elif globals()['p1_n'+str(i)] == 'J' :
                                globals()['p1_n'+str(i)] = 10
                            elif globals()['p1_n'+str(i)] == 'Q' :
                                globals()['p1_n'+str(i)] = 10
                            elif globals()['p1_n'+str(i)] == 'K' :
                                globals()['p1_n'+str(i)] = 10
                            else :
                                pass
                        c_over += int(globals()['p1_n'+str(len(cpu))])
                        c_possible = 1
                    elif stay_num > 3 :
                        c_possible = 2
            else :
                pass

            if p_over > c_over :
                if p_over > 21 :
                    print(f'\n{player}')
                    print(f'Player : {p_over}')
                    print(f'\n{cpu}')
                    print(f'C P U : {c_over}')
                    print('CPU 승리')
                    print('')
                    p_money -= b_money
                    c_money += b_money                    
                    g_switch = 1                  
                else :
                    print(f'\n{player}')
                    print(f'Player : {p_over}')
                    print(f'\n{cpu}')
                    print(f'C P U : {c_over}')
                    print('Player 승리')
                    print('')
                    p_money += b_money
                    c_money -= b_money                    
                    g_switch = 1
                    
            elif p_over < c_over :
                if c_over > 21 :
                    print(f'\n{player}')
                    print(f'Player : {p_over}')
                    print(f'\n{cpu}')
                    print(f'C P U : {c_over}')
                    print('Player 승리')
                    p_money += b_money
                    c_money -= b_money                    
                    print('')
                    g_switch = 1               
                else :
                    print(f'\n{player}')
                    print(f'Player : {p_over}')
                    print(f'\n{cpu}')
                    print(f'C P U : {c_over}')
                    print('CPU 승리')
                    print('')
                    p_money -= b_money
                    c_money += b_money                    
                    g_switch = 1

            elif p_over == c_over :
                print(f'\n{player}')
                print(f'Player : {p_over}')
                print(f'\n{cpu}')
                print(f'C P U : {c_over}')                
                print('Draw')
                g_switch = 1
                
        elif act != 1 and act != 2 :
            print('올바른 행동을 선택해주세요\n')



if p_money > c_money :
    print('Player 최종승리')
elif p_money < c_money :
    print('CPU 최종승리')


#p1_p1 = f'{random.choice(deck)}'[:1]
#p1_n1 = f'{random.choice(deck)}'[1:]
#p1_c1 = p1_p1+p1_n1
    
'''
test = []
for i in  range(1, 10, 1) :
    pick = f'{random.choice(deck)}'
    locals()['p1_p'+str(i)]= pick[:2]
    locals()['p1_n'+str(i)] = pick[2:]
    locals()['p1_c'+str(i)] = locals()['p1_p'+str(i)]+locals()['p1_n'+str(i)]
    test.append(locals()['p1_c'+str(i)])
    deck = list(set(deck)-set(test))
    #deck.remove(locals()['p'+str(i)+'_c'+str(i)])

test.sort()
print(test)




p1_p1 = f'{random.choice(pat)}'
p1_n1 = f'{random.choice(num)}'
p1_p2 = f'{random.choice(pat)}'
p1_n2 = f'{random.choice(num)}'

player = [f'{p1_p1}'+f'{p1_n1}',f'{p1_p2}'+f'{p1_n2}']

c1_p1 = f'{random.choice(pat)}'
c1_n1 = f'{random.choice(num)}'
c1_p2 = f'{random.choice(pat)}'
c1_n2 = f'{random.choice(num)}'

cpu = [f'{c1_p1}'+f'{c1_n1}',f'{c1_p2}'+f'{c1_n2}']

if p1_n1 == 'A' :
    p1_n1 = int(1)
elif p1_n1 == 'J' :
    p1_n1 = int(10)
elif p1_n1 == 'Q' :
    p1_n1 = int(10)
elif p1_n1 == 'K' :
    p1_n1 = int(10)    
else :
    pass

if p1_n2 == 'A' :
    p1_n2 = int(1)
elif p1_n2 == 'J' :
    p1_n2 = int(10)
elif p1_n2 == 'Q' :
    p1_n2 = int(10)
elif p1_n2 == 'K' :
    p1_n2 = int(10)    
else :
    pass

if c1_n1 == 'A' :
    c1_n1 = int(1)
elif c1_n1 == 'J' :
    c1_n1 = int(10)
elif c1_n1 == 'Q' :
    c1_n1 = int(10)
elif c1_n1 == 'K' :
    c1_n1 = int(10)    
else :
    pass

if c1_n2 == 'A' :
    c1_n2 = int(1)
elif c1_n2 == 'J' :
    c1_n2 = int(10)
elif c1_n2 == 'Q' :
    c1_n2 = int(10)
elif c1_n2 == 'K' :
    c1_n2 = int(10)    
else :
    pass

p1_n1 = int(p1_n1)
p1_n2 = int(p1_n2)

c1_n1 = int(c1_n1)
c1_n2 = int(c1_n2)

# print(f'{p1_n1},{p1_n2}')
# print(f'{p1_n1+p1_n2}')


    
act = 0
turn = 1
p_over = p1_n1 + p1_n2
c_over = c1_n1 + c1_n2


while act != 2 :
    print(player)
    print('총 합 :',p_over)
    print('1. Hit   2. Stand')
    act = int(input('행동을 선택하세요 : '))
    if act == 1 :
        globals()['p1_p'+str(turn+2)] = f'{random.choice(pat)}'
        globals()['p1_n'+str(turn+2)] = f'{random.choice(num)}'
        player.append(globals()['p1_p'+str(turn+2)]+globals()['p1_n'+str(turn+2)])
        if globals()['p1_n'+str(turn+2)] == 'A' :
          globals()['p1_n'+str(turn+2)] = int(1)
        elif globals()['p1_n'+str(turn+2)] == 'J' :
            globals()['p1_n'+str(turn+2)] = int(10)
        elif globals()['p1_n'+str(turn+2)] == 'Q' :
            globals()['p1_n'+str(turn+2)] = int(10)
        elif globals()['p1_n'+str(turn+2)] == 'K' :
            globals()['p1_n'+str(turn+2)] = int(10)    
        else :
            pass
        p_over += int(globals()['p1_n'+ str(turn+2)])
        if p_over > 21 :
            print(f'\n{player}')
            print('총 합 :',p_over)
            print('BUST!')
            act = 2
        turn += 1        
        print('\n')
    elif act != 1 and act != 2 :
        print('올바른 행동을 선택해주세요\n')
    elif act == 2 :
        pass
    
'''
