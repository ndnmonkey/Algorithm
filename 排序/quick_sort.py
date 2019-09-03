'''
基本思想：
1．先从数列中取出一个数作为基准数。
2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。
'''
def quick_sort(list):
    if len(list) == 1:
        return list
    else:
        base = list[0]
        left = []
        right = []
        for i in list:
            if i>=base:
                right.append(i)
            else:
                left.append(i)
        return combine(left,right)
#合并两个排好的list
def combine(left,right):
    left.extend(right)
    sort_list = sorted(left)
    return sort_list

l = [5,1,7,3,4,4,0,2,6]
result = quick_sort(l)
print(result)