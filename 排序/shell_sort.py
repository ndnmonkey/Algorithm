def shell_sort(list,gap):
    #导入的list的长度
    length = len(list)
    #gap为0则停止，不为0则继续迭代
    if gap == 0:
        return list
    else:
        #list_container用于装按照gap打散（分组）后的列表
        list_container = []
        for i in range(0,gap):
            temp_list = []
            for j in range(i,length,gap):
                temp_list.append(list[j])
            # print(temp_list)
            list_sep = sort(temp_list)
            list_container.append(list_sep)
        print("按照对应gap划分出的列表：",list_container)

        sorted_list = sort_all_list(list_container, length, gap)
        print("调用sort_all_list后:",sorted_list)
        #gap减小以达到最终迭代终止条件
        gap = gap//2
        #最后调用自己以迭代
        return shell_sort(sorted_list, gap)

def sort(list1):
    return sorted(list1)
#把按照gap打散（分组）后的列表排到一个理好顺序的list中
def sort_all_list(list2,length,gap):
    new_list = []
    for mm in range(length):
        new_list.append(0)
    #把l2每个数组按照每隔gap组成一个new_list
    for list in list2:
        N = list2.index(list)
        for i in range(N,length,gap):
            num = int((i-N)/gap)
            new_list[i] = list[num]
    # print("sort_all_list:",new_list)
    return new_list

l = [9,1,3,6,87,12,64,9,11,65,7]
#初始gap
if len(l) % 2 == 0:
    gap = int(len(l) / 2)
else:
    gap = int((len(l) - 1) / 2)
shell_sort(l,gap)


'''
l2 =[[3, 7, 9], [1, 4], [2, 8], [5, 6]]
length = 9
gap = 4
print(4/4)

def sort_all_list(list2,length,gap):

    new_list = []
    for mm in range(length):
        new_list.append(0)

    #把l2每个数组按照每隔gap组成一个new_list
    for list in list2:
        N = list2.index(list)
        for i in range(N,length,gap):
            num = int((i-N)/gap)
            new_list[i] = list[num]
    return new_list

sort_all_list(l2,length,gap)
'''