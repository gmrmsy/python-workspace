import os

pat = None
main_menu = 0

while main_menu != 3 :
    os.system("cls")
    print('{:□^26}'.format(' 무늬계단 만들기 '))
    print(f'1. 계단 만들기   현재무늬 : {pat}')
    print('2. 무늬 선택')
    print('3. 종료')
    print('□'*33)
    print()
    main_menu = int(input('선택해주세요>>> '))
    print()
    

    if main_menu == 1 :
        if pat == None :
            print('무늬를 먼저 선택해주세요!')
            print()
            os.system("pause")
        elif pat != None :
            N = int(input('줄 갯수를 입력하세요 : '))
            print()
            for i in range(1,N+1) :
                print(pat*i)
            print()
            print('계단 완성!')
            print()
            os.system('pause')
        main_menu = 0


    elif main_menu == 2 :
        print('1. *   2. □   3. ￦   4. 입력')
        pat_manu = int(input('무늬를 선택해주세요>>> '))
        print()
        if pat_manu == 1 :
            pat = '*'
            print(f'{pat}을 선택하셨습니다!')
            main_menu = 0
            print()
            os.system('pause')
        elif pat_manu == 2 :
            pat = '□'
            print(f'{pat}을 선택하셨습니다!')
            main_menu = 0
            print()
            os.system('pause')
        elif pat_manu == 3 :
            pat = '￦'
            print(f'{pat}을 선택하셨습니다!')
            main_menu = 0
            print()
            os.system('pause')
        elif pat_manu == 4 :
            pat = input('무늬를 입력하세요>>> ')
            print(f'{pat}을 선택하셨습니다!')
            main_menu = 0
            print()
            os.system('pause')
        else :
            print('정확히 입력해주세요!')
            print()
            os.system('pause')


    elif main_menu == 3 :
        pass


    else : 
        print('다시 입력해주세요')
        os.system('pause')
        print()