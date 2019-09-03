def niu(n):
    '''
    :param n:第n年
    :return: 第n年总牛数
    '''
    if n <= 4:
        return n
    else:
        return niu(n-1) + niu(n-3)
print(niu(4))