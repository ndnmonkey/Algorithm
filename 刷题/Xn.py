'''
求x的n次幂
'''
def A(x,n):
    if n == 1 :
        return x
    else:
        if n%2 == 0:
            return A(x,n/2)*A(x,n/2)
        else:
            return A(x,(n+1)/2)*A(x,(n-1)/2)
re = A(3,9)
print(re)