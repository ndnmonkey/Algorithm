#冒泡的方式，O(kn)，缺点：时间复杂度大了点，关键是改变了原有的输入数组。
def TopK(arr,k):
    for j in range(k):
        for i in range(len(arr)-1):
            if arr[i] >arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        print(arr[len(arr)-j-1])

TopK([3,6,4,2,11,10,5,1],3)
