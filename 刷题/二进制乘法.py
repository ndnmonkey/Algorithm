def mul(a,b):
    count = 1
    if a < 0:
        count = -count
        a = -a
    if b < 0:
        count = -count
        b = -b

    sum = 0
    while(b!=0):
        if (b&1!=0):
            sum = sum + a
            print(sum)
        a = a<<1
        b = b>>1
    return  sum if count > 0 else -sum
mul(1,11)

