'''
i = 3


globals()['p1_p'+str(i)] = f'{random.choice(pat)}'
globals()['p1_n'+str(i)] = f'{random.choice(num)}'

# p'f'{i}''_p'f'{i}'' = f'{random.choice(pat)}'
# p'f'{i}''_n'f'{i}'' = f'{random.choice(num)}'

# print(f'{p1_p3}'+f'{p1_n3}')


player = []


p1_draw = f'{random.choice(pat)}'+f'{random.choice(num)}'
p2_draw = f'{random.choice(pat)}'+f'{random.choice(num)}'
player.append(f'{p1_draw}')
player.append(f'{p2_draw}')






p1_n1 = player[0][1:]
p1_n2 = player[1][1:]
'''

# print(p1_n1)
# print(p1_n2)

import random

pat = ['♥', '◆', '♣', '♠']
num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

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


    
A_c = 0
turn = 1
p_over = p1_n1 + p1_n2
c_over = c1_n1 + c1_n2


while A_c != 2 :
    print(player)
    print('총 합 :',p_over)
    print('1. Hit   2. Stand')
    A_c = int(input('행동을 선택하세요 : '))
    if A_c == 1 :
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
            print(player)
            print('\n총 합 :',p_over)
            print('BUST!')
            A_c = 2
        turn += 1        
        print('\n')
    elif A_c != 1 and A_c != 2 :
        print('올바른 행동을 선택해주세요\n')
    elif A_c == 2 :
        pass
    

