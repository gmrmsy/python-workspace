

#import day2.elif05
#print("현재페이지")

import os

#data = 0;
data = None


while True:
    print("="*30)
    print("1.데이터 입력")
    print("2.데이터 출력")
    print("3.종료")
    print("="*30)
    num = input(">>> : ")
    if num == "1":
        data = input("데이터 입력 => ")
    elif num == 2:
        if data == None:
            print("저장 데이터 없음")
        else:
            print("입력 데이터 : ",data)
        os.system("pause")
    elif num == 3:
        os._exit(1)
    os.system("cls")    








