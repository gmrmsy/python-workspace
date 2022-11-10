pat = ['◆', '♠', '♣', '♥']
num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = []

player = []
ply_pat = []
ply_num = []


cpu = []
cpu_pat = []
cpu_num = []

comty = []
com_pat = []
com_num = []




import random
from collections import Counter

### 덱 생성 ###
pat = ['◆', '♠', '♣', '♥']
num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = []

for i in pat :
    for k in num :
        deck.append(f'{i}'+f'{k}')
############

### 기본 카드 ###

def draw(one) :
    one_pat = []
    one_num = []
    for i in  range(2) :
        pick = f'{random.choice(globals()[deck])}'
        locals()[one[0]+'1_p'+str(i)] = pick[:1]
        locals()[one[0]+'1_n'+str(i)] = pick[1:]
        locals()[one[0]+'1_c'+str(i)] = locals()[one[0]+'1_p'+str(i)]+locals()[one[0]+'1_n'+str(i)]
        one_pat.append(locals()[one[0]+'1_p'+str(i)])
        one_num.append(locals()[one[0]+'1_n'+str(i)])    
        one.append(locals()[one[0]+'1_c'+str(i)])
        deck = list(set(deck)-set(one))

ply = []
draw(ply)

print(ply_pat)
