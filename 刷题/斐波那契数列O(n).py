def Fb(n):
    if n < 0:
        return -1
    if n <2:
        return 1
    a = 1
    b = 1
    for i in range(n):
        temp = a + b
        a,b = b,temp
    print(a)
Fb(4)