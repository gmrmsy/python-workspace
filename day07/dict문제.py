key = 0
dict = {}

while key != 6 :

    print('1. 인적사항 등록')
    print('2. 검색')
    print('3. 수정')
    print('4. 삭제')
    print('5. 전체학생 보기')
    print('6. 종료')
    
    key = int(input('>>> '))
    print()

    if key == 1 :
        num = int(input('학번 입력 : '))
        if dict.get(num) != None :
            print('존재하는 학번입니다.')
            continue
        name = input('이름 입력 : ')
        grade = input('등급 입력 : ')
        adress = input('주소 입력 : ')
        dict_1 = {'학번': num, '이름':name, '등급':grade, '주소':adress}
        dict[num] = dict_1

        print()
        print('등록 완료')

    if key == 2 :
        search = int(input('찾고자하는 학생 학번 입력 : '))
        if dict.get(search) == None :
            print('찾고자 하는 학생이 없습니다')
            print()
        elif dict.get(search) != None :
            print(f'학번 : {dict[search]["학번"]}')
            print(f'이름 : {dict[search]["이름"]}')
            print(f'등급 : {dict[search]["등급"]}')
            print(f'주소 : {dict[search]["주소"]}')
            print()

    if key == 3 :
        num = int(input('학번을 입력하세요 : '))
        if dict.get(num) == None :
            print('등록되지 않은 학번입니다')
            continue
        elif dict.get(num) != None :
            print('*학번 수정은 삭제 후 재등록해주세요')
            print('1) 이름   2) 등급   3)주소')
            num_ = int(input('>>> '))

            if num_ == 1 :
                dict[num]['이름'] = input('새로운 이름을 입력하세요 : ')
            if num_ == 2 :
                dict[num]['등급'] = input('새로운 등급을 입력하세요 : ')
            if num_ == 3 :
                dict[num]['주소'] = input('새로운 주소을 입력하세요 : ')

    if key == 4 :
        num_ = int(input('삭제할 학번을 입력하세요 : '))
        if dict.get(num_) == None :
            print('등록되지 않은 학번입니다')
            continue 
        elif dict.get(num_) != None :
            del(dict[num_])
            print('삭제되었습니다.')
            print()

    if key == 5 :
        for k, v in dict.items() :
            for kk, vv in v.items() :
                print(f'{kk} : {vv}')
            print('-'*15)    
        print()
        