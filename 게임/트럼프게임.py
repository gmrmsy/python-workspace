import random

pat = ['♥', '◆', '♣', '♠']
num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

player = []
p1_draw = f'{random.choice(pat)}'+f'{random.choice(num)}'
p2_draw = f'{random.choice(pat)}'+f'{random.choice(num)}'
player.append(f'{p1_draw}')
player.append(f'{p2_draw}')
print(player)

p1_n1 = player[0][1:]
p1_n2 = player[1][1:]

print(p1_n1)
print(p1_n2)


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

print(f'{p1_n1},{p1_n2}')

p1_n1 = int(p1_n1)
p1_n2 = int(p1_n2)

print(f'{p1_n1+p1_n2}')




# print(int(f'{player[1][2]}') + int(f'player[2][2]}'))


'''
while choice == 1 :
    turn = 0
    draw = [f'{random.choice(pat)}+random.choice(num)']
    player.append(f'draw')
    print('
    turn_c = int(input('행동을 선택하세요 : ')
    if 
'''
