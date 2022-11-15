st = '  Life is good  '

# 공통적으로 print를 하지 않으면 아무런 결과값을 보이지 않는다.

### 문자열 길이 ###
len = len(st)
print(len)



### 문자열 찾기, 검색 ###
fin = st.find('i')
print(fin)
# st.find('a',b) b이후에 a가 언제 나오는지 찾기
fin = st.find('i',4) 
print(fin)



### 대소문자 변경 ###
upp = st.upper()   # 전부 대문자로
print(upp)

low = st.lower()   # 전부 소문자로
print(low)

swa = st.swapcase()   # 대소문자 변환
print(swa)



### 공백처리 ###
str = st.strip()  # 양쪽 공백 없애기
print(str)
st_ = '--Life is good--'
str_ = st_.strip('-')  # 양끝에서부터 해당문자가 아닌게 나올때까지 다지워
print(str_)
rst_ = st_.rstrip('-')  # 오른쪽에서부터 해당문자가 아닌게 나올때까지 다지워
print(rst_)
lst_ = st_.lstrip('-')  # 왼쪽에서부터 해당문자가 아닌게 나올때까지 다지워
print(lst_)



### 정렬 ###
cen = st.center(20)        # center(a,'b') a만큼 공간확보하고
cen_ = st.center(20,'-')   # 가운데 정렬, 남은부분은 'b'로 채우기

lju = st.ljust(20)        # ljust(a,'b') a만큼 공간확보하고
lju_ = st.ljust(20,'-')   # 왼쪽 정렬, 남은부분은 'b'로 채우기

rju = st.rjust(20)        # rjust(a,'b') a만큼 공간확보하고
rju_ = st.rjust(20,'-')   # 오른쪽 정렬, 남은부분은 'b'로 채우기



### 문자열 수정 ###
rep = st.replace('good', 'nice')
print(rep)   # replace('a','b') a를 b로 바꾸기

spl = st.split()  # 빈칸일 경우 공백을 기준으로 나누기
print(spl)        # 나눠진 데이터는 리스트형식으로 저장
spl = st.split('i')   # split('a') a 를 기준으로 나누기
print(spl)

st = '''
안녕하 세 요
안녕하 세 요
안녕하 세 요
'''
spl_li = st.splitlines()   # 줄바꿈기준으로 나누는 명령어 존재
print(spl_li)
spl = st.split('\n')   # 이렇게해도 다를바 없음
print(spl)



### 깍지끼기 ###
st = '123'
test = '%'

joi_1 = test.join(st)
print(joi_1)   # 'a'.join(str) str문자열 사이사이에 'a'를 넣는다
joi_2 = '$'.join(st)
print(joi_2)   # 'a'는 변수, 문자가능
joi_4 = st.join('안녕 하 세요')
print(joi_4)   # 띄어쓰기 포함!

### 다른 문자열명령어와 순서가 다르다!!

li = ['', '123', '456']
print('그래'.join(li))   # str위치에 리스트도 가능
# 리스트도 가능하다 / 개체 사이에 해당문자 넣고 하나의 문자열로 출력



### 문자열 구성요소 ###

st = 'python te12st 1234'
st_ = 'pythonte12st1234'
st__ = 'python test'
st___ = '123412341234'
st____ = 123412341234
st_____ = 'PYTHON TE12ST 1234'

print(st.isdigit())   # 숫자로만 구성
print(st_.isdigit())
#print(st____.isdigit())   # 문자열만 가능! int 안된다!
print(st___.isdigit())
print(st[9:11].isdigit())
print()

print(st.isalpha())   # 영어로 구성
print(st_.isalpha())
print(st__.isalpha())
print(st[0:6].isalpha())   # 공백없이 문자만있는지!
print()

print(st.isalnum())   # 알파벳+숫자로만 구성
print(st_.isalnum())   # 공백포함되면 false
print(st[7:13].isalnum())
print()

print(st.islower())
print(st_____.islower())   # 대문자 하나만있어도 false
print()

print(st.isupper())
print(st_____.isupper())   # 숫자 상관없다
print()

print(st.isspace())
print(st[6].isspace())   # 공백'만' 존재하는지!


st = 'Have a nice day'
print( st.count('a') )  # 해당 갯수 세기
print( st.count('day') )  # 단어 단위로도 가능
print( st.count('daY') )  # 대소문자 구분
print( st.startswith('Ha') )  # 시작하는 문자가 맞는지
print( st.startswith('ha') )  # 대소문자 구분
print( st.endswith('day') )  # 끝나는 문자가 맞는지
print( st.endswith('dda') )  # 대소문자 구분



