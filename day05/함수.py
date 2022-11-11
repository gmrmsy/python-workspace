def self_num(num):
    ls = []
    for i in range(1, num) :
        #print(i,': start')
        while i < num-1 :
            i += i//1000 + (i%1000)//100 + (i%100)//10 + (i%10)
            ls.append(i)
            #print(i)
    #print(ls)

    a = []
    for i in range(1,num) :
        a.append(i)

    ls.sort()
    ls = set(ls)
    a = set(a)
    a = a - ls
    a = list(a)
    a.sort()

    return a

s = self_num(10)

print(s)
print()



def han_(num) :

    count = 0
    for i in range(1,num+1) :

        if 1< i < 100 :
            count += 1

        elif 100 <= i < 1000 :
            if (i%100)//10 - i//100 == i%10 - (i%100)//10 :
                count += 1
            else :
                pass

    return count


a = han_(1000)
print(a)