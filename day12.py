#####  12일차 #####
'''
Tuple
- 중복된 데이터를 가질수 없다
- 데이터 변경이 불가능
- index로 접근 가능하다
- 소괄호가 있으면 튜플로 보면 된다.
'''
tp = (10,20,30)
print( 'tp :', tp )
print('tp[0] :',tp[0])
print('type(tp) : ', type(tp) )
print('len(tp) :', len(tp) )

#tp[0] = 1000
tp = (111,222,333,444)
print('tp :', tp)

print("-"*20)
tp = (10)
print(type(tp))

tp = (10,)
print(type(tp))

tp = 10,
print(type(tp))

'''
packing : 압축(여러개의 값을 가지고 있다)
unpacking : 하나의값을 여러개로 나누는 것
'''
pack = 1,2,"패킹"
print("패킹 : ", pack)
print( type(pack) )

a,b,c = pack
print(a,b,c)

a, *b = pack
print(a,b)
print(type(a), type(b))  # 다시 패킹할때는 리스트로 묶인다

pack = 10,20,10,10,30
print( pack.count(10) )
print( pack.index(20) )

print("-"*20)
str_ = "Have a nice day"
print(str_[0])
print(str_[1])

print("-"*20)
li = [1,2,3,4]
print( li[-1] )
print( str_[-1] )

print("-"*20)
for i in range( len(str_) ):
    print( str_[i], end=" " )
print()
for i in str_:
    print(i, end=" ")
print()
print(str_[7:11])
print("-"*20)
str_ = "Python test. 그리고 programming 할만하다 ^^"
print( str_ )
print("upper : ",str_.upper() )  # 대문자로 변환
print("lower : ",str_.lower() )  # 소문자로 변환
print("swapcase :", str_.swapcase() )  # 대소문자 변환
print("title :", str_.title())  # 띄어쓰기 기준 처음 나오는 모든 알파벳 대문자 변환
                                       # 나머지 알파벳은 소문자로 변환

print("-"*20)
asd = "NevEr -eVer 110gIVe up"
# asd = asd.lower()
print(asd.title())
print("-"*20)

st = 'Have a nice day'
print( st.count('a') )  # 해당 갯수 세기
print( st.count('day') )  # 단어 단위로도 가능
print( st.count('daY') )  # 대소문자 구분
print( st.startswith('Ha') )  # 시작하는 문자가 맞는지
print( st.startswith('ha') )  # 대소문자 구분
print( st.endswith('day') )  # 끝나는 문자가 맞는지
print( st.endswith('dda') )  # 대소문자 구분

print("-"*20)
st = 'It is a fun Python class'
print(st.count(''))
print( len(st) )
print(st.count('a'))
print(st.count('s'))

print("-"*20)
st = 'Have a nice day'
print(st)
print(st.find('day'))
print(st.index('day'))
print(st.find('a'))  # 첫번째 'a'의 위치만 찾아준다
print(st.find('a', 2))  #2번칸부터 찾아라
print(st.find('a', 6))  # 6번칸부터 찾아라
print(st.find('a', 14)) # 14번칸부터 찾아라
c = st.find('a', 2)
print(c)
c = st.find('a', c+1)
print(c)

print("-"*20)
print(st.find('ㅁㄴㅇㄹ'))  # 해당 값이 없을 때 없음(-1) 표시
print("print(st.index('kkk'))  # 해당 값이 없을 때 오류로 작동중지")

print("-"*20)
st = 'Have a nice day Have a nice day Have a nice day'
index = []
c = 0
while True :
    c = st.find('a', c)
    if c > 0 :
        index.append(c)
        c += 1
    else :
        break
print(index)


print("-"*20)
st = 'Have a nice day Have a nice day Have a nice day'
index = []
for i in range( len(st) ) :
    if st[i] == 'a' :
        index.append(i)
    else :
        pass
print(index)
print(a)

print("-"*20)
li = ['AbCe test123', '.acd efg', 'a123 TEST 123', '123 TEst']

for i in li :
    ad = i.lower()
    if ad.startswith('ab') == True :
        print(i)
    elif ad.endswith('test') == True :
        print(i)
    
print("-"*20)
st = '2015/04/02'

print(st)
st1 = st.replace('/','.')
print(st)
print(st1)

print("-"*20)
st = '''
김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월 14일
'''
print(st)
st_1 = st.replace('-',': ')

print(st_1)
print(st_1[1:4])
st_2 = st_1.replace(st_1[1:4],'이효재')
print(st_2)
c = 0

while True :
    if st_1.find(':',c) > 0 :
        c = st_1.find(':', c)
        st_1 = st_1.replace(st_1[c+2:c+6],'1999')
        c += 1
    else :
        break
    
print(st_1)
