def redtea(list,cup):
    list = sorted(list)
    a= []
    for i in list:
        if cup - i in list:
            a.append(i)

    for j in a:
        if j == cup - j:
            a.pop(a.index(j))
    # print(a)
    b= []
    for k in range(len(a)//2):
        print(a[k],cup-a[k])

redtea([2,4,6,1,3,5,7],7)