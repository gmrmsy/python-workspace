import copy

aa =  [ [1,2,3,4], [5,6,7,8] ]

a = aa[0]
a[1] = 2000

print('aa : ',id(aa),aa)
print('a : ',id(a),a)
print('')

aa =  [ [1,2,3,4], [5,6,7,8] ]

a = aa[0][:]
a[1] = 2000

print('aa : ',id(aa),aa)
print('a : ',id(a),a)
print('')

aa =  [ [1,2,3,4], [5,6,7,8] ]

a = copy.deepcopy(aa[0])
a[1] = 3000

print('aa : ',id(aa),aa)
print('a : ',id(a),a)
print('')


ls_2 = []
for i in range(3) :
    ls_1 = []
    for k in range(1,5) :
        value = 4*i + k
        ls_1.append(value)
        if k != 4 :
            print(value,end='\t')
        if k == 4 :
            ls_2.append(ls_1[:])
            print(value)
print(ls_2)


ls_1 = []
ls_2 = []
value = 1

for i in range(3) :
    for k in range(4) :
        ls_1.append(value)
        value += 1
    ls_2.append(ls_1)
    ls_1 = [] 

print(ls_2)

arr = [1,2,3]
arr2 = arr

arr2.clear()  # 참조하고 있는 데이터공간을 초기화하는 것
print(arr)     #같은 데이터공간을 공유하는 변수도 초기화가 된다


ls_2 = [ [6548,56,48,651], [65,984], [651,984,61,9816,15,2] ]
for i in ls_2 :
    #print(i)
    for k in i :
        print(k,end='\t')
    print()
'''
for i in range(3) :
    for k in range(4) :
        print(ls_2[i][k],end='\t')
    print()
'''

be = ['2019', '12', '31']

be = map(int,be) # 리스트 안에 변수형식 한번에 변환, / (list,set,dict 등등) map(문자형식, 변수)
print(list(be))

be = [ ['100','222'], ['200','300'] ]
print(be)
for i in range( len(be) ) :
    for k in range( len(be[i]) ) :
        be[i][k] = int(be[i][k])
print(be)


be = [ ['100','222'], ['200','300'] ]
print(be)
for i in range( len(be) ) :
    be[i] = list(map(int, be[i]))
print(be)

be[0][0] = be[0][0] * 100
print(be)

for i in range( len(be) ) :
    be[i] = list( map(str, be[i] ))
print(be)


ls = [
      [['이름'], ['나이'], ['주소'],['지울값'], ['연봉']],
      [['홍길동'], ['20살'], ['산골자기'], ['지우세요'], ['5000']],
      [['김개똥'], ['30살'], ['지구촌'], ['지우세요'], ['4500']]
      ]
print(ls)
print()

for i in range(len(ls)) :
    for j in range(len(ls[i])) :
        print(ls[i][j],end='')
    print()


for i in range(len(ls)) :
    del(ls[i][3])
print()

for i in range(len(ls)) :
    for j in range(len(ls[i])) :
        print(ls[i][j],end='')
    print()

print(ls)
print(ls[1][3][0])
print(str(int(ls[1][3][0])*1.1))

for i in range(len(ls)) :
    if i != 0 :
        ls[i][3][0] = str(int(int(ls[i][3][0])*1.1))
    
print(ls)
