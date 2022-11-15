st = {'학번':1234, '이름':'홍길동'}

print(st)
print()

print(st.items())
print()


# for i in st.keys():
for k, v in st.items() :
    print(f'{k} : {v}')

print(st.setdefault('학번1',55555))   # key와 value를 추가
print(st)                            # key가 중복되면 무효

ls = [10, {'키':'키에의한값'}, 30]

print(ls[0])
print(ls[1]['키'])
print(ls[2])

dic = ls[1]

print(ls[1], ls[1]['키'], dic['키'])

dic = {'li':[10,20,30], 'k':'value'}

print(dic['li'])
print(dic['li'][0])
print(type(dic['li'][0]))
print(dic['k'])
print()


info_1 = {}
info_2 = {}

info_2['가수'] = '개가수'
info_2['인원'] = 3
info_2['노래'] = '신나리'

info_1[ info_2['가수'] ] = info_2

print(info_2)
print(info_1)

for k, v in info_1.items() :
    print(k)
    print(v)
    for kk, vv in v.items() :
        print(kk,':',vv)
        
info_2['안녕'] = '하세요'

print(info_1)
print()




info_2 = {}

print(info_1)
print(info_2)
print()

info_2['가수'] = '개가수'
info_2['인원'] = 3
info_2['노래'] = '신나리'

info_1[ info_2['가수'] ] = info_2.copy()

info_2['안녕'] = '하세요'

print(info_1)
print()


