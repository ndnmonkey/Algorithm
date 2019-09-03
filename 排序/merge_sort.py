def merge_sort(list):
    if len(list) == 1:
        return list
    else:
        mid = len(list)//2  #地板除
        left = list[:mid]
        right = list[mid:]
        return merge(left,right)
#合并两个排好的list
def merge(left,right):
    left.extend(right)
    sort_list = sorted(left)
    return sort_list

result = merge_sort([9,1,7,3,4,8,2,6])
print(result)