import random

dic = {'A':int(1), 'J':int(11), 'Q':int(12), 'K':int(13)} 

pat = ['♥', '◆', '♣', '♠']
num = [f'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', f'J', f'Q', f'K']

player = []
f1_draw = f'{random.choice(pat)}'+f'{random.choice(num)}'
f2_draw = f'{random.choice(pat)}'+f'{random.choice(num)}'
player.append(f'{f1_draw}')
player.append(f'{f2_draw}')
print(player)

i1 = player[0][1]
i2 = player[1][1]

print(i1)
print(i2)


if i1 == 'A' or 'J' or 'Q' or 'K' :
    if i1 == 'A' :
        i1 = int(1)
    if i1 == 'J' or 'Q' or 'K' :
        i1 = int(10)

if i2 == 'A' or 'J' or 'Q' or 'K' :
    if i2 == 'A' :
        i2 = int(1)
    if i2 == 'J' or 'Q' or 'K' :
        i2 = int(10)

i1 = int(i1)
i2 = int(i2)

print(f'{i1+i2}')

# 숫자 두자리일 경우 (10) 어떻게 뽑을 지
# 숫자 합을 어떻게 구현할지

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
