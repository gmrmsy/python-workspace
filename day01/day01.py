print('test python')
print( 3 + 5 )
print('안\n녕\t하\'세\\요\"')
print()
print('\t\t#### 회비 정보 ####\t\t')
print('='*48)
print('이름\t\t나이\t전화번호\t회비')
print('='*48)
print('홍길동\t\t15\t010-123-1234\t\\20,000')
print('임꺽정\t\t20\t010-234-2345\t\\30,000')
print('김말이\t\t28\t010-345-3456\t\\50,000')
print('-'*48)
print('총합계\t\t\t\t\t\\100,000')
print('='*48)

name = ['홍길동', '임꺽정', '김말이', '이효재']
age = ['15', '20', '28', '29']
number = ['010-123-1234', '010-234-2345', '010-345-3456', '010-2236-0760']
money = ['20000', '30000', '50000', '100000']

total = 0
for i in range(len(money)) :
    total += int(money[i])


print('\t\t#### 회비 정보 ####\t\t')
print('='*48)
print('이름\t\t나이\t전화번호\t회비')
print('='*48)
for i in range(len(name)) :
    print('{0}\t\t{1}\t{2}\t\\{3:,}'.format(name[i], age[i], number[i], int(money[i])))

print('-'*48)
print('총합계\t\t\t\t\t\\{0:,}'.format(total))
print(f'총합계\t\t\t\t\t\\{total:,}')
print('총합계\t\t\t\t\t\\{}'.format(total, ',d'))
print('='*48)
print()
print('{0:,}'.format(total))
print(f'{total:,}')
print(format(total, ',d'))
print()
print('{0}\t\t{1}\t{2}\t\\{3:,}'.format(name[i], age[i], number[i], int(money[i])))
print(f'{name[i]}\t\t{age[i]}\t{number[i]}\t\\{int(money[i]):,}')
print('{}\t\t{}\t{}\t\\{}'.format(name[i], age[i], number[i], int(money[i]), ',d'))
print()

print('12 + 54 =',12+54,'입니다')
print('268 - 42 =',268-42,'입니다')
print('2 * 23 =',2*23,'입니다')
print('120 / 3 =',120/3,'입니다')
print()

print('12 + 54 = {} 입니다'.format(12+54))
print('268 - 42 = {} 입니다'.format(268-42))
print('2 * 23 = {} 입니다'.format(2*23))
print('120 / 3 = {} 입니다'.format(120/3))


print('1234567\t1')
print('12345678\t1')
print('123456789\t1')