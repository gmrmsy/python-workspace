'''
현재 시간(O월O일O시O분)과 소요시간 입력하고
현재 시간부터 소요시간 후에 완료 시간(O월O일O시O분)이 되는지 출력되는 프로그램
(말일은 30일로 통일한다)

'''





# 쉬움

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