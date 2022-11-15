st = 'NevEr-eVer 110gIVe up'

lo = st.lower()
up = st.upper()
title = st.title()

print(lo)
print(up)
print(title)



st = '안녕하세요 오늘 2300/5/4 날씨는 error 춥다'

sp = st.split()
time = sp[2]

del(sp[2])
del(sp[3])

sp.insert(2, time[0:4]+'년'+time[5]+'월'+time[-1]+'일')

print(sp)

st = ''

for i in sp :
    st += i+' '

print(st)


print(' '.join(sp))


st = 'python'
print(st)
print(st.center(10))
print(st.center(10,'-'))

print(st.ljust(10))
print(st.ljust(10,'-'))

print(st.rjust(10))
print(st.rjust(10,'-'))




accountBook = 'shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000'

print('item\tdate\t$(price)')
print('-'*25)

ab = accountBook.split(', ')

for i in ab :
    k = i.split()
    k[2] = format(int(k[2]), ',')
    print(f'{k[0]}\t{k[1]}\t${k[2]}')

print()
print()


accountBook = 'shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000'

print('item\tdate\t$(price)')
print('-'*25)

ab = accountBook.split(', ')

for i in ab :
    k = i.split()
    for j in range(len(k)) :
        if j == 0 :
            print(k[j],end='\t')
        if j == 1 :
            print(k[j],end='\t')
        if j == 2 :
            k[j] = format(int(k[j]), ',')        
            print('$'+k[j])


print()
print()


accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
replaceAB = accountBook.split(',')#,기준으로 리스트로 저장
k=0
for i in replaceAB:
    replaceAB[k]=i.lstrip() #각 문자열의 왼쪽 공백 삭제 후 저장(_coffee,_food,_dress)
    k+=1
kk='$ '
print('item'.ljust(10),end='')
print('date'.ljust(10),end='')
print('$(price)'.ljust(10))
for i in range(len(replaceAB)):
    z=replaceAB[i].split() #공백을 기준으로 리스트로 저장
    for k in range(len(z)):
        if k == 0 :
            print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력
        elif k ==1 :
            print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력
        elif k == 2 : 
            print("{:,}".format(int(z[k])).join(kk).ljust(10)) 
                ############ 기억해두자 ############


print()
print()




st = {'stNum':1234, '이름':'홍길동'}
print(st)
print(type(st))
'''
impo = {}
name = input('등록할 키 입력 : ')
value = input('등록할 값 입력 : ')
impo[name] = value
print(impo)
print(impo[name])
'''
num = {1:'일', 2:'이', 3:'삼'}
print(num.keys())
print(num.values())

# print(num.keys()[0])  딕셔너리는 []으로 찾기 불가능!!

print(type(num.keys()))

li = list(num.keys())   # 리스트로 형변환해서 뽑을 수 있다!

print(li,li[0])

for i in num.keys() :
    print(i,':',num[i])
print()
00
num = {1:'일', 2:'이', 3:'삼'}
print(num[1])
print(num.get(1))


print(num.get(11))   # 없으면 None으로 출력
#print(num[11])      # 없으면 에러!



product = {}
key = 0

while key != 4 :
        
    print('1. 메뉴 등록')
    print('2. 메뉴별 가격 보기')
    print('3. 가격 수정')
    print('4. 종료')
    key = int(input('>>> '))
    print()

    if key == 1 :
        menu = input('메뉴 입력 : ')
        if product.get(menu) != None :
            print('등록되어 있습니다!!!')
            print()
            continue
        price = input('가격 입력 : ')
        print()
        product[menu] = price
    
    elif key == 2 :
        for i in list(product) :
            print(f'{i} : {product[i]}')
            print()
    
    elif key == 3 :
        cor = input('수정할 목록 입력 : ')
        print()
        if product.get(cor) == None :
            print('등록을 먼저하세요!!')
            print()
        if product.get(cor) != None :
            product[cor] = int(input('수정가격 : '))
            print()

    elif key == 4 :
        pass

    else : 
        print('다시 한 번 입력해주세요')
        print()

