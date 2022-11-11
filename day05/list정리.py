ls = [1, 2, 5, 4, 3, 6, 7]

# 요소 끄집어내기 : ()입력값 꺼내기 (리스트에서는 제거)
#                  입력값 없으면 맨 뒤부터
print(ls)
print('print(ls.pop())')
print(ls.pop())#
print()

# 깊은복사
print(ls)
print('print(ls.copy())')
print(ls.copy())#
print()

# 개수세기 : ()입력값 개수세기
print(ls)
print('print(ls.count(1))')
print(ls.count(1))#
print()

# 위치반환 : ()입력값이 어느위치에 있는지
print(ls)
print('print(ls.index(5))')
print(ls.index(5))#
print()

# 리스트 정렬
print(ls)
print('print(ls.sort())')
print(ls.sort())
print()

# 요소추가
print(ls)
print('print(ls.append(8))')
print(ls.append(8))
print()

# 확장 : ()에는 리스트만 입력가능, 기존리스트뒤로 입력리스트추가
print(ls)
print('print(ls.extend([9, 0]))')
print(ls.extend([9, 0]))
print()

# 요소삽입 : (a,b) a위치에 b삽입
print(ls)
print('print(ls.insert(8, 0))')
print(ls.insert(8, 0))
print()

# 요소제게 : ()입력값 제거 (맨 뒤부터)
print(ls)
print('print(ls.remove(0))')
print(ls.remove(0))
print()

# 리스트 뒤집기
print(ls)
print('print(ls.reverse())')
print(ls.reverse())
print()

# 데이터공간 초기화 : 얕은복사본도 초기화된다
print(ls)
print('print(ls.clear())')
print(ls.clear())