st = "Have a nice day"

print( st )

print( st[0] )
print( st[1] )
print( st[-1] )

print( len(st) )


st = "Have a nice day"
for i in st:
    print(i, end="")
print()

for i in range( len(st) ):
    print(st[i], end="")
print("="*20)

st = "Have a nice day"
print( st[3:6] )

st = "Python test. 그리고 programming 할만하다 ^^"
print( st )
print( st.upper() )#대문자로 변경
print( st.lower() )#소문자로 변경
print( st.swapcase() )# 상호변경. 대/소문자
print( st.title() )#단어의 첫번째 대문자로 변경

st = 'NevEr -eVer 110gIVe up'
st = st.title()
print(st)

print("="*10)
st = "Have a nice day"
print(st)
print( st.count('a') )
print( st.count('day') )
print( st.count('dak') )

print( st.startswith('Ha'))#시작문자
print( st.startswith('ha'))

print( st.endswith('day') )#끝 문자
print( st.endswith('da') )

st = "It is a fun Python class"
print( len(st) )
print( st.count('a') )
print( st.count('s'))

print("="*10)
st = "Have a nice day"
print(st)
print( st.find('day') )
print( st.index('day') )
print( st.find('dddd') )
#print( st.index('dddd') )
st = "Have a nice day"

num = st.find('a')
print( st.find('a') )
print( st.find('a',num+1) )

num = st.find('a',num+1)
print( st.find('a',num+1) )
print( st.find('a',14) )






st = 'Have a nice day Have a nice day Have a nice day'
cnt = 0
ls = []
while True:
    cnt = st.find('a' , cnt )
    if cnt != -1:
        ls.append( cnt )
        cnt += 1
    else:
        break
print('a 개수 : ' , st.count('a') )
print('index : ' , ls )



li = ['AbCe test123', '.acd efg', 'a123 TEST 123', '123 TEst']
for i in li:
    lo = i.lower()
    if lo.startswith('ab') or lo.endswith('test'):
        print(i)

st = '   파이썬   '
print(f"*{st}*")
print(f"*{st.strip()}*")
'''
name = input("이름 입력 : ")
print("이름 : ",name)
if name.strip() == '홍길동':
    print("인증통과")
else:
    print("인증실패!!!")
'''

st = "+++파 이 썬+++"
print(st)
print( st.strip("+") )
print( st.rstrip("+") )
print( st.lstrip("+") )

print("="*10)
st ="2015/04/02"
print( st )
print( st.replace("/", ".") )
print( st.replace(st[0:4], "2022") )


st = """
aaaa
bbbbb
cccc
dddd
eeee
"""
print(st)













