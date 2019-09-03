'''
若list长度为n则迭代n-1次，每次迭代只要有前面大于后面便交换
'''
def buble_sort(list):
    n = 1
    while len(list)-n:
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
        n +=1
        print(n-1,":",list)

l = [3,6,4,2,11,10,5,1]
buble_sort(l)