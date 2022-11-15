n = int(input('인원수를 입력하세요 : '))
n_ = 0
big ={}
while True :

    name = input(f'{n_+1}번 째 학생이름>>> ')
    weight = int(input(f'{n_+1}번 째 학생몸무게>>> '))
    height = int(input(f'{n_+1}번 째 학생키>>> '))
    big[name] = {'몸무게':weight, '키':height, '등수':1}
    n_ += 1
    if n_ == n :
        break


for i in big :
    for k in big :
        if i == k :
            pass
        elif big[i]['몸무게'] > big[k]['몸무게'] and big[i]['키'] > big[k]['키'] :
            pass
        elif big[i]['몸무게'] > big[k]['몸무게'] or big[i]['키'] > big[k]['키'] :
            pass
        elif big[i]['몸무게'] < big[k]['몸무게'] and big[i]['키'] < big[k]['키'] :
            big[i]['등수'] += 1


print('이름\t몸무게\t키\t등수')
for i in big :
    print(f'{i}',end='\t')
    for k in big[i] :
        print(f'{big[i][k]}',end='\t')
    print()