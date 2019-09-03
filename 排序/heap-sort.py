#调整树的三个节点，但不能调整调整后的下层节点,不过不影响最大值到根节点来。
def adjuste_tree(non_leaf, list):
    # 一定注意得先验证最后一个非叶子节点是否有右子节点。
    if len(list) == 1 or len(list) == 0:
        return list
    else:
        if non_leaf == int(len(list)/2-1):  #是否是最后一个非叶子节点
            if 2*non_leaf+2 == len(list)-1:  #这个最后一个非叶子节点是否有右子节点
                if list[non_leaf] < list[2 * non_leaf + 1] or list[non_leaf] < list[2 * non_leaf + 2]:
                    if (list[2 * non_leaf + 1] > list[2 * non_leaf + 2]):
                        list[non_leaf], list[2 * non_leaf + 1] = list[2 * non_leaf + 1], list[non_leaf]
                        # print("Left:", list[non_leaf], [2 * non_leaf + 1], [2 * non_leaf + 2])
                    elif (list[2 * non_leaf + 1] < list[2 * non_leaf + 2]):
                        list[non_leaf], list[2 * non_leaf + 2] = list[2 * non_leaf + 2], list[non_leaf]
                        # print("Right:",list[non_leaf],[2 * non_leaf + 1],[2 * non_leaf + 2])
            else: #进入这里证明没有右子节点
                if list[non_leaf] < list[2*non_leaf+1]:  #这个最后一个非叶子节点是否比它的左子节点大
                    list[2 * non_leaf + 1], list[non_leaf] = list[non_leaf], list[2 * non_leaf + 1]
        else:
            if list[non_leaf] < list[2 * non_leaf + 1] or list[non_leaf] < list[2 * non_leaf + 2]:
                if (list[2 * non_leaf + 1] > list[2 * non_leaf + 2]):
                    list[non_leaf], list[2 * non_leaf + 1] = list[2 * non_leaf + 1], list[non_leaf]
                elif (list[2 * non_leaf + 1] < list[2 * non_leaf + 2]):
                    list[non_leaf], list[2 * non_leaf + 2] = list[2 * non_leaf + 2], list[non_leaf]

def Heap_sort(list):
    #1,建堆,以找出最大值
    #第一个非叶子节点为len/2-1
    n = int(len(list) / 2 - 1)
    for non_leaf in range(n,-1,-1):  #根节点序号为0时也要排序
        #若节点小于他的子节点。
        adjuste_tree(non_leaf, list)

if __name__ == '__main__':
    list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    soted_heap_list = []

    #2,取出根再调整堆
    #3,重复2直到只剩下一个数
    while(len(list)):
        Heap_sort(list)
        soted_heap_list.append(list.pop(0))
    print(soted_heap_list)