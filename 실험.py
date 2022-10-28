import random
from collections import Counter

### 덱 생성 ###
pat = ['◆', '♠', '♣', '♥']
num = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'J', 'K', 'Q']
deck = []

for i in pat :
    for k in num :
        deck.append(f'{i}'+f'{k}')
############

player = []
p_pat = []
p_num = []
for i in  range(10) :
    pick = f'{random.choice(deck)}'
    locals()['p1_p'+str(i)]= pick[:1]
    locals()['p1_n'+str(i)] = pick[1:]
    locals()['p1_c'+str(i)] = locals()['p1_p'+str(i)]+locals()['p1_n'+str(i)]
    p_pat.append(locals()['p1_p'+str(i)])
    p_num.append(locals()['p1_n'+str(i)])
    player.append(locals()['p1_c'+str(i)])    
    deck = list(set(deck)-set(player))



print(player)
p_pat_count = Counter(p_pat)
p_num_count = Counter(p_num)

print(dict(p_pat_count))
print(dict(p_num_count))
