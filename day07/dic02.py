st = {"stNum":1234, "이름":"홍길동"}
print( st )
print( type(st) )

mobile = {"품명":"겔럭시","가격":1000}
print( mobile )
print( mobile['품명'] )

impo = {}
impo['파이썬'] = "www.python.org"
impo['네이버'] = 'www.naver.com'
print( impo )
print(impo['파이썬'])
print(impo['네이버'])

impo = {}
name = input("등록할 키 입력 : ")
value = input("등록할 값 입력 : ")
impo[name] = value
print( impo )
print( impo[name] )

num = {1:"일", 2:"이", 3:"삼"}
print( num.keys() )
print( num.values() )


print( type(num.keys()) )
#print( num.keys()[0] )
li = list(num.keys())
print(li , li[0])

for i in num.keys():
    print( i,":", num[i] )
    
print("-"*10)
num = {1:"일", 2:"이", 3:"삼"}
print( num[1] )
print( num.get(1) )

#print( num[111] )
print( num.get(111) )

key = int(input("key 입력 : ") )
result = num.get(key)
if result == None:
    print("찾는 내용이 없습니다")
else:
    print(key,":",result )



menu={};  bl = True;  num = 0
while bl:
    print("1.메뉴 등록"); print("2.메뉴별 가격 보기");
    print("3.가격 수정");print("4.종료")
    num=int(input(">>> "))
    if num == 1:
        name = input("메뉴 입력 : "); 
        if menu.get(name) != None:
            print("등록되어 있습니다!!!")
        else:   menu[name] = input("가격 입력 : ")
    elif num == 2:
        for i in menu.keys():
            print(i,":",menu[i])
    elif num == 3:
        name = input("수정할 목록 입력 : ");
        if menu.get(name) == None:
            print("등록 먼저 하세요!!")
        else:    menu[name] = input("수정가격 : ")
    elif num ==4:
        print("프로그램 종료 합니다")
        bl = False












