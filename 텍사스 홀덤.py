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

### 기본 카드 ###
player = []
p_pat = []
p_num = []
for i in  range(2) :
    pick = f'{random.choice(deck)}'
    locals()['p1_p'+str(i)]= pick[:1]
    locals()['p1_n'+str(i)] = pick[1:]
    locals()['p1_c'+str(i)] = locals()['p1_p'+str(i)]+locals()['p1_n'+str(i)]
    p_pat.append(locals()['p1_p'+str(i)])
    p_num.append(locals()['p1_n'+str(i)])    
    player.append(locals()['p1_c'+str(i)])
    deck = list(set(deck)-set(player))

cpu = []
c_pat = []
c_num = []
for i in  range(2) :
    pick = f'{random.choice(deck)}'
    locals()['c1_p'+str(i)]= pick[:1]
    locals()['c1_n'+str(i)] = pick[1:]
    locals()['c1_c'+str(i)] = locals()['c1_p'+str(i)]+locals()['c1_n'+str(i)]
    c_pat.append(locals()['c1_p'+str(i)])
    c_num.append(locals()['c1_n'+str(i)])    
    cpu.append(locals()['c1_c'+str(i)])
    deck = list(set(deck)-set(cpu))
##############

### Community Card ###

# Flop 
comty = []
t_pat = []
t_num = []
for i in  range(3) :
    pick = f'{random.choice(deck)}'
    locals()['t1_p'+str(i)]= pick[:1]
    locals()['t1_n'+str(i)] = pick[1:]
    locals()['t1_c'+str(i)] = locals()['t1_p'+str(i)]+locals()['t1_n'+str(i)]
    t_pat.append(locals()['t1_p'+str(i)])
    t_num.append(locals()['t1_n'+str(i)])    
    comty.append(locals()['t1_c'+str(i)])
    deck = list(set(deck)-set(comty))

# Turn
pick = f'{random.choice(deck)}'
t1_p4= pick[:1]
t1_n4 = pick[1:]
t1_c4 = t1_p4+t1_n4
t_pat.append(t1_p4)
t_num.append(t1_n4)
comty.append(t1_c4)
deck = list(set(deck)-set(comty))

# River
pick = f'{random.choice(deck)}'
t1_p5= pick[:1]
t1_n5 = pick[1:]
t1_c5 = t1_p5+t1_n5
t_pat.append(t1_p5)
t_num.append(t1_n5)
comty.append(t1_c5)
deck = list(set(deck)-set(comty))

##### 족보 #####
p_pat_count = dict(Counter(p_pat+t_pat))
p_num_count = dict(Counter(p_num+t_num))
c_pat_count = dict(Counter(c_pat+t_pat))
c_num_count = dict(Counter(c_num+t_num))




print(comty)
print('')
print(player)
print(dict(p_pat_count))
print(dict(p_num_count))
print('')
print(cpu)
print(dict(c_pat_count))
print(dict(c_num_count))
print('')

for i in p_num :
    if p_num_count[i] == 2 :
        print(f'{i} 원페어')
        
for i in p_num :
    if p_num_count[i] == 3 :
        print(f'{i} 트리플')

