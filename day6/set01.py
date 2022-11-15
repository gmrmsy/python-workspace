'''
set
- 중복된 데이터 허용하지 않음
- 순서를 유지하지 않는다
사용방법
- set(데이터)
- {값, 값,,,,}
'''
s = {"안녕하세요"}
print( s )
print( type(s) )

s = set([1,1,1,2,3,4,4])
print( s )
#print( s[0] )

li = list(s)
print( li )
print( li[0] )

s = {1,2,3}
print('변경 전 : ',s)
s.add(555)
print('변경 후 :',s)
s.update([4,5,6])
print( s )
s.remove(555)
print('remove(555) :', s )
print("issuperset : ", s.issuperset({1,2}) )















