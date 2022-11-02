'''
set
- 중복을 허용하지 않는다.
- 순서가 없다
- list처럼 index로 접근이 불가능
'''
s = set('안녕녕녕하세요')
print(s)
print( type(s) )

s = set([1,2,3,3,3,'안','안','녕'])
print(s)
#print( s[0] )

li = list(s)
print( li )
print( type(li) )
print( li[0] )

li = [1,2,3]
li.append("aaa")
print(li)

s = {1,2,3,4}
print(s)
print( type(s) )

s.add(555)
print(s)

s.update([7,8,9])
print(s)

s.remove(555)
print( s )

print( s.issuperset({9,1,3}) )


import random

for i in range(5):
    print( random.random(), end=", ")

print()
for i in range(5):
    print( int(random.random()*3), end=", ")

print()
for i in range(6):
    print( random.randrange(1,46), end=", ")

print("-"*20)
s = set()

print('s : ', len(s))
while len(s) < 6 :
    s.add( random.randrange(1,46) )
print(s)

li = list()
while len(li) < 6 :
    ran = random.randrange(1,46)
    if li.count( ran ) == 0:
        li.append( ran )
print(li)











