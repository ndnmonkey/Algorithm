def F(n):
    a = 1
    b = 1
    if n <= 2:
        return 1
    else:
        for i in range(2,n):
            a,b = b,a+b
        return b
print(F(5))