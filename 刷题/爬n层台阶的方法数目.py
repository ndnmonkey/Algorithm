'''
一次可以跨1或2个台阶，爬到n层有多少种方法？
这里时间复杂度为：O(2^n)
'''
def taijie(n):
    if n < 2:
        return n
    else:
        return taijie(n-1)+taijie(n-2)
print(taijie(3))