def Add(a,b):
    while (b!=0):
        # print(format(a, 'b'))
        a,b = a^b,(a&b)<<1
    return a
print(Add(-11,3))