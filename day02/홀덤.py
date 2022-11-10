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
ply = []
ply_pat = []
ply_num = []
for i in  range(2) :
    pick = f'{random.choice(deck)}'
    locals()['p1_p'+str(i)]= pick[:1]
    locals()['p1_n'+str(i)] = pick[1:]
    locals()['p1_c'+str(i)] = locals()['p1_p'+str(i)]+locals()['p1_n'+str(i)]
    ply_pat.append(locals()['p1_p'+str(i)])
    ply_num.append(locals()['p1_n'+str(i)])    
    ply.append(locals()['p1_c'+str(i)])
    deck = list(set(deck)-set(ply))

cpu = []
cpu_pat = []
cpu_num = []
for i in  range(2) :
    pick = f'{random.choice(deck)}'
    locals()['c1_p'+str(i)]= pick[:1]
    locals()['c1_n'+str(i)] = pick[1:]
    locals()['c1_c'+str(i)] = locals()['c1_p'+str(i)]+locals()['c1_n'+str(i)]
    cpu_pat.append(locals()['c1_p'+str(i)])
    cpu_num.append(locals()['c1_n'+str(i)])    
    cpu.append(locals()['c1_c'+str(i)])
    deck = list(set(deck)-set(cpu))
##############

### Community Card ###

# Flop 
com = []
com_pat = []
com_num = []
for i in  range(3) :
    pick = f'{random.choice(deck)}'
    locals()['t1_p'+str(i)]= pick[:1]
    locals()['t1_n'+str(i)] = pick[1:]
    locals()['t1_c'+str(i)] = locals()['t1_p'+str(i)]+locals()['t1_n'+str(i)]
    com_pat.append(locals()['t1_p'+str(i)])
    com_num.append(locals()['t1_n'+str(i)])    
    com.append(locals()['t1_c'+str(i)])
    deck = list(set(deck)-set(com))

# Turn
pick = f'{random.choice(deck)}'
t1_p4= pick[:1]
t1_n4 = pick[1:]
t1_c4 = t1_p4+t1_n4
com_pat.append(t1_p4)
com_num.append(t1_n4)
com.append(t1_c4)
deck = list(set(deck)-set(com))

# River
pick = f'{random.choice(deck)}'
t1_p5= pick[:1]
t1_n5 = pick[1:]
t1_c5 = t1_p5+t1_n5
com_pat.append(t1_p5)
com_num.append(t1_n5)
com.append(t1_c5)
deck = list(set(deck)-set(com))

##### 족보 밑작업 #####

# 숫자, 패턴 카운팅
ply_pat_count = dict(Counter(ply_pat+com_pat))
ply_num_count = dict(Counter(ply_num+com_num))
cpu_pat_count = dict(Counter(cpu_pat+com_pat))
cpu_num_count = dict(Counter(cpu_num+com_num))

# 숫자 랭크
rank_num = {}
append_num = []
st_rank_num = {}
for i in range(2,15) :
    append_num.append(i)

for i in range(13) :
    rank_num[num[i]] = append_num[i]

for i in range(13) :
    st_rank_num[append_num[i]] = num[i]


# 최종 숫자, 최종 카드
ply_result_num = ply_num+com_num
cpu_result_num = cpu_num+com_num
ply_com = ply + com
cpu_com = cpu + com


# 숫자 정렬

sort_ply_result_num = []
for i in ply_result_num :
    sort_ply_result_num.append(rank_num[i])
sort_ply_result_num.sort()

ply_result_num = []
for i in sort_ply_result_num :
    ply_result_num.append(st_rank_num[i])

sort_cpu_result_num = []
for i in cpu_result_num :
    sort_cpu_result_num.append(rank_num[i])
sort_cpu_result_num.sort()

cpu_result_num = []
for i in sort_cpu_result_num :
    cpu_result_num.append(st_rank_num[i])


print('공유카드')
print(com)
print('')
print('플레이어 카드')
print(ply)
print('')
print('CPU카드')
print(cpu)
print('')




ply_pair = 0
ply_pair_num = []
for i in list(set(ply_result_num)) :
    if ply_num_count[i] == 2 :
        ply_pair += 1
        ply_pair_num.append(i)

ply_triple = 0
ply_triple_num = []
for i in list(set(ply_result_num)) :
    if ply_num_count[i] == 3 :
        ply_triple += 1
        ply_triple_num.append(i)

ply_fourcard = 0
ply_fourcard_num = []
for i in list(set(ply_result_num)) :
    if ply_num_count[i] == 4 :
        ply_fourcard += 1
        ply_fourcard_num.append(i)

ply_flush = 0
for i in ply_pat :
    if ply_pat_count[i] > 4 :
        ply_flush = 1
        ply_flush_pat = i



if ply_flush == 1 :
    for i in ply_com :
        if i[0] == ply_flush_pat :
            print(i,end=' ')    
    print('플러쉬')

elif ply_fourcard == 1 :
    for i in ply_com :
        if i[1:] == ply_fourcard_num[0] :
            print(i,end=' ')
    print('포카드')

elif ply_triple > 0 :
    if ply_triple == 2 :
        if ply_triple_num[0] > ply_triple_num[1] :
            for i in ply_com :
                if i[1:] == ply_triple_num[0]:
                    print(i,end=' ')
            print('트리플')
        if ply_triple_num[0] < ply_triple_num[1] :
            for i in ply_com :
                if i[1:] == ply_triple_num[1]:
                    print(i,end=' ')
            print('트리플')
    elif ply_triple == 1 :
        if ply_pair > 0 :
            if ply_pair == 2 :
                if ply_pair_num[0] > ply_pair_num[1] :
                    for i in ply_com :
                        if i[1:] == ply_triple_num[0] :
                            print(i,end=' ')
                    for i in ply_com :
                        if i[1:] == ply_pair_num[0] :
                            print(i,end=' ')
                    print('풀하우스')
                if ply_triple_num[0] < ply_triple_num[1] :
                    for i in ply_com :
                        if i[1:] == ply_triple_num[0] :
                            print(i,end=' ')
                    for i in ply_com :
                        if i[1:] == ply_pair_num[1] :
                            print(i,end=' ')
                    print('풀하우스')
            if ply_pair == 1 :
                for i in ply_com :
                    if i[1:] == ply_triple_num[0] :
                        print(i,end=' ')
                
                    if i[1:] == ply_pair_num[0] :
                        print(i,end=' ')
                print('풀하우스')
        if ply_pair == 0 :
            for i in ply_com :
                if i[1:] == ply_triple_num[0] :
                    print(i,end=' ')
            print('트리플')

elif ply_pair > 0 :
    if ply_pair > 1 :
        highest = rank_num[ply_pair_num[0]]
        high_num = ply_pair_num[0]
        for i in ply_pair_num :
            if highest < rank_num[i] :
                highest = rank_num[i]
                high_num = i
        for i in ply_com :
            if i[1:] == high_num :
                print(i,end=' ')
        ply_pair_num.remove(high_num)
        for i in ply_com :
            if i[1:] == ply_pair_num[0] :
                print(i,end=' ')
        print('투페어')
       
    if ply_pair == 1:
        for i in ply_com :
            if i[1:] == ply_pair_num[0] :
                print(i,end=' ')
        print('원페어')

else :
    highest = rank_num[ply_result_num[0]]
    high_num = ply_result_num[0]
    for i in ply_result_num :
        if highest < rank_num[i] :
            highest = rank_num[i]
            high_num = i
    for i in ply_com :
        if i[1] == high_num :
            print(i,end=' ')
    print('하이카드')





print(ply_pair,end='  ')
print(ply_triple,end='  ')
print(ply_fourcard,end='  ')
print()
asd = ply_result_num.sort()
print(asd)
