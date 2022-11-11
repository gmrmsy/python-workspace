'''
import os
a = 0
ls = []
while True :

    while True :
        print('ls :',ls)
        a = (input('리스트에 들어갈 숫자를 입력하세요>>> '))
        if a == 'e' or a == 'E' :
            break
        ls.append(a)


    os.system('cls')
    print('='*30)
    print('1. reverse   2. sort   3. 종료')
    num = int(input('>>>>> '))
    print()

    if num == 1 :
        print(ls.reverse())
        os.system('pause')
    elif num == 2 :
        print(ls.sort()) 
        os.system('pause')
    elif num == 3 :
        break
    else :
        print('다시 입력해주세요')
'''
