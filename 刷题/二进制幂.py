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
        a = a<<1
        b = b>>1
    return  sum if count > 0 else -sum


def power(a,b):
    flag1 = 1
    flag2 = 1
    if a < 0:
        a = -a
        flag1 = -flag1
    if b < 0:
        b = -b
        flag2 = -flag2
    if b%2 == 0:
        flag1 = -flag1

    multi = 1
    while(b!=0):
        if (b&1!=0):
            multi = mul(multi,a)
        a = mul(a,a)
        b = b>>1
    if flag1 < 0:
        if flag2 < 0:
            return -1/multi
        else:
            return -multi
    else :
        if flag2 < 0:
            return 1/multi
        else:
            return multi

    return multi
print(power(2,-3))