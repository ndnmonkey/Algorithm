# 把n个盘子移从a移到c
def hanoi(n,a,b,c):
    if n == 1:
        print("{0}-->{1}".format(a,c))
    else:
        # 把n-1个盘子移从a移到b
        hanoi(n-1, a, c, b)
        # 把1个盘子移从a移到c
        print("{0}-->{1}".format(a, c))
        # 把n-1个盘子移从b移到c
        hanoi(n - 1, b, a, c)

hanoi(3,"a","b","c")