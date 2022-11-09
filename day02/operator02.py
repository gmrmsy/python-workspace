n1, n2 = 9, 2 

print(f'{n1} + {n2} = {n1+n2}')
print(f'{n1} * {n2} = {n1*n2}')
print(f'{n1} / {n2} = {n1/n2}')
print(f'{n1} // {n2} = {n1//n2}')
print(f'{n1} % {n2} = {n1%n2}')
print(f'{n1} ** {n2} = {n1**n2}')
print()



num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
num2 = [1,2,3,4,5,'5','6']

print(num+num2)









'''
현재 시간(O월O일O시O분)과 소요시간 입력하고
현재 시간부터 소요시간 후에 완료 시간(O월O일O시O분)이 되는지 출력되는 프로그램
* 말일
    쉬움 : (말일은 30일로 통일한다)
    보통 : 1,3,5,7,8,10,12월 - 31일
           4,6,8,9,11월 - 30
           2월 - 28일
    어려움 : 2월이 29일까지 있는 윤년은 4년마다 돌아오며 가장 최근 윤년은 2022년이다


예시) 현재시간입력 : 11월 8일 23시 25분
      소요시간 : 140분

      예상시간 : 11월 9일 1시 45분

'''





# 쉬움
'''
print('현재시간을 입력해주세요')
year = int(input('년 : '))
month = int(input('월 : '))
day = int(input('일 : '))
hour = int(input('시 : '))
minute = int(input('분 : '))

print(f'현재 시간은 {year}년 {month}월 {day}일 {hour}시 {minute}분 입니다.')
print()

time = int(input('소요시간을 입력하세요 : (분)'))
print()

if minute + time > 61 :
    hour += time // 60
    minute = time % 60
if hour > 25 :
    day += hour // 24
    hour = hour % 24
if day > 31 :
    month += day // 30
    day = day % 30
if month > 13:
    year += month // 12
    month = month % 12

print(f'예상시간은 {year}년 {month}월 {day}일 {hour}시 {minute}분 입니다.')


'''
# 보통

print('현재시간을 입력해주세요')
year = int(input('년 : '))
month = int(input('월 : '))
day = int(input('일 : '))
hour = int(input('시 : '))
minute = int(input('분 : '))

print(f'현재 시간은 {year}년 {month}월 {day}일 {hour}시 {minute}분 입니다.')
print()

time = int(input('소요시간을 입력하세요 : '))
print()

if minute + time > 61 :
    hour += time // 60
    minute = time % 60

if hour > 25 :
    day += hour // 24
    hour = hour % 24

while day > 27 :
    if month == 2 :
        month += 1
        day -= 28
    elif month == 4 or month == 6 or month == 8 or month == 9 or month == 11 :
        month += 1
        day -=30
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        month += 1
        day -= 31

if month > 13:
    year += month // 12
    month = month % 12

print(f'예상시간은 {year}년 {month}월 {day}일 {hour}시 {minute}분 입니다.')

