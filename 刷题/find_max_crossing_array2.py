'''
# 动态规划法求最大子数组
求最大子数组问题.
时间复杂度：O(n)

计算前 n 项和，这是一个前缀，判断只要前缀是大于零的那么加上后一位就是越来越大的。一直向后相加就可以了。
一旦前缀小于零，就是说前 n 项和小于零了。那么那个前缀形成的子数组不可能在变大，所以要开始新的前缀（新的子数组）。
'''
def max_child(arr):
    result = arr[0]
    sum = arr[0]
    x = 0
    for i in range(1, len(arr)):
        if sum > 0:
            sum += arr[i]
        else:
            sum = arr[i]
            x = i
        if sum > result:
            result = sum
            y = i
    print("最大子数组的起始-结束下标", arr[x:y+1])
    return result

arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print("最大子数组的和：",max_child(arr))