print( 20 + 200 )
print ("안녕하세여") #문자열일 경우 ""(큰따옴표) 혹은 ''(작은따옴표) 사이에 작성
print ( 100 ) ; print ( 2000 ) # ;(세미클론) 마침표의 의미 이거 안쓰면 문장이 계속된다고 인식한다.
# 이거는 포함 안되지롱

# ''는 한줄은 커버가 안된다

'''안녕
하세요'''

# '''     ''' 으로 묶으면 여러줄 커버가능

print("""안
      녕
      하
      세
      요 """)
print("\n")


'''
ESCAPE 문자 - 문자열 안에서 특수한 동작을 해주는 것
                     - \n : 엔터값과 비슷하다
                     - \t : tap크기만큼 커서를 오른쪽으로 이동 (빈칸안에 앞 내용을 채워넣는다, 8자이상이면 다시8칸 추가)
                     - \" : "(큰따옴표) 출력
                     - \' : '(작음따옴표) 출력
'''

print("안\n녕\n하\n세\n요")
print(" Have\ta\t\tgood\ttime")
print("1234567\t1\t12345678\t55")
print("이름\t나이\t성별\t비고")
print("이효재\t29\t남\t파이썬")
print("\n")

print(" '안녕' '''' ")
#print(" "안녕" ")  오류가 생긴다
print(" \"안녕\" ")
print( "C:\\Users\\user\\Documents\\k-디지털" ) # \하나만 사용시 오류가 날 수도 있다
print( "C:\\Users\\user\\Documents\\k-디지털" )
print( "C:/Users/user/Documents/k-디지털" )
print("\n")

print("="*48)
print("\t\t####회비정보####")
print("=="*24)
print("==="*16)
print("이름\t\t나이\t전화번호\t\t회비")
print("===="*12)
print("======"*8)
print("홍길동\t\t\"15\"\t010-123-1234\t|20,000")
print("임꺽정\t\t\"20\"\t010-234-2345\t|30,000")
print("김말이\t\t\"28\"\t010-345-3456\t|50,000")
print("========"*6)
print("============"*4)
print("총합계\t\t\t\t\t|100,000")
print("================"*3)
print("\n")

print("\t\t####회비정보####\n================================================\n이름\t\t나이\t전화번호\t\t회비\n================================================\n홍길동\t\t\"15\"\t010-123-1234\t|20,000\n임꺽정\t\t\"20\"\t010-234-2345\t|30,000\n김말이\t\t\"28\"\t010-345-3456\t|50,000\n================================================\n총합계\t\t\t\t\t|100,000")
print("\n")

print(1+2+3+4+6)
print(6-4-3-2-1)
print(1*2*3*4*6)
print(6/4/3/2/1)
print(' 안녕' , 123+123)  #문자열, 숫자열 서로다른 문장을 넣을때는 ,(콤마)로 구분
print('100') #보기에는 숫자열이지만 문자열로 읽힌다
print('100'+'100')
print("안녕"+"디지몬")
print("\n")


print("12 + 54 =",12 + 54,"입니다")
print("268 - 48 =",268 - 48,"입니다")
print("2 * 23 =",2*23,"입니다")
print("120 / 3 =",120/3,"입니다")
print("\n")

print(f"12+54= {12+54} 입니다")  # f 문자열 안에 숫자열작성
print(f"268 - 48 = {268 - 48} 입니다")
print(f"2 * 23 = {2 * 23} 입니다")
print(f"120 / 3 = {120 / 3} 입니다")
print("\n")

print("12+54= {} 입니다".format(12+54))
print("{}+{}= {} 입니다".format(10,20,30))
print("{2}+{1}= {0} 입니다".format(10,20,30))
print("\n")

print("{:,}".format(10000000000000))
print("{:<10}왼쪽정렬{:<10}".format('안녕','하세'))
print("{:<10}왼쪽정렬{:0<10}".format('안녕','하세'))
print("{:>10}오른쪽정렬{:>10}".format('안녕','하세'))
print("{:>10}오른쪽정렬{:8>10}".format('안녕','하세'))
print("{:^10}가운데정렬{:^10}".format('안녕','하세'))
print("{:^10}가운데정렬{:6^10}".format('안녕','하세'))
print("\n")


'''
변수
- 데이터를 저장하기 위한 공간
- 데이터는 언제든지 변경 가능하다
- 의미를 부여해서 만든다
- 키워드(예약어)는 사용할 수 없다 ex)print, format
- 한글로 이름할 수 있으나 영어로 만드는 것이 좋다
'''

# =  대입 연산자 / 오른쪽에 있는 결과값을 왼쪽에 저장한다
num = 1000
print("저장값",num,"입니다")
print(f"저장값 {num}입니다")
print("저장값{}입니다".format(num))

num = 5
print( '변경후',num)   # 뒤에 같은 이름으로 설정하면 갱신된다

num = num + 100
print('연산 후 :',num)   # 대입 연산자는 오른쪽에 있는 결과값을 왼쪽에 저장하는거기 때문에 오른쪽num은 5가 들어가지 않는다

num1 = 5
num2 = 10
Sum = num1+num2
print('n1 :',num1)
print('n2 :',num2)
print('sum:',Sum)


num1 = 10
num2 = 20
print("{:-^20}".format(" 출력 결과 "))
print("num1({}) + num2({}) = {}".format(num1,num2,num1+num2))
print("\n")

num1 = 10
num2 = 20
print("{:-^20}".format(" 출력 결과 "))
print(f"num1({num1}) + num2({num2}) = {num1+num2}")
print("\n")
