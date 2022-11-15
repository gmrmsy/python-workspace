st = {"학번":1234, "이름":"홍길동"}
print( st )
print( st.items() )
#for i in st.keys():
for k, v in st.items():
    print(f"{k} : {v}")

st = {"학번":1234, "이름":"홍길동"}
print(st.setdefault("학번1",5555) )
print( st )

print("="*10)

ls = [10,{"키":"키에의한값"},30]
print( ls[0] )
dic = ls[1]
print( ls[1], ls[1]["키"], dic["키"] )
print( ls[2] )

dic = {"li":[10,20,30], "k":"value"}
print( dic["li"], dic["li"][2] )
print( dic["k"] )

info = {}
info02 = {}

info02['가수'] = "개가수"
info02['인원수'] = 3
info02['노래명'] = "신나리"
info[ info02['가수'] ] = info02.copy()

print( info02 )
print( info )
print("-"*10)
for k, v in info.items():
    #print(k)
    #print(v)
    for kk, vv in v.items():
        print(kk,":",vv)

print("-"*10)
info02['안녕'] = "하세요"

print( info )
print( info02 )

info = {}
info.clear()













