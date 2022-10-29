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

asdf = {}
rank_num = {}
append_num = []
for i in range(2,15) :
    append_num.append(i)

for i in range(13) :
    rank_num[num[i]] = append_num[i]

print(rank_num)

if pair > 0 :
    if pair == 2 :
        if rank_num[triple_num[0]] > rank_num[triple_num[1]] :
            print(f'{triple_num[0]} 투페어')
        if rank_num[triple_num[0]] < rank_num[triple_num[1]] :
            print(f'{triple_num[1]} 투페어')
    if pair == 1 :
        print 


        if pair_num[0] > pair_num[1] :
            print(f'{pair_num[0]} 투페어')
        if triple_num[0] < triple_num[1] :
            print(f'{pair_num[1]} 투페어') 