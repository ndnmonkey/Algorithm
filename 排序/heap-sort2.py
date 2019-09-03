#调整树的三个节点，调整调整后的下层节点。
def adjuste_tree(heap,root):
    HeapSize = len(heap)
    #有右子节点 且  （左节点 > 根  or  右节点 > 根）
    if 2*root+2 <= len(heap)-1 and (heap[2*root+2] > heap[root] or heap[2*root+1] > heap[root]):
        if heap[2*root+1] > heap[2*root+2]:
            heap[2 * root + 1], heap[root] = heap[root], heap[2 * root + 1]
            adjuste_tree(heap, 2 * root + 1)
        else:
            heap[2 * root + 2], heap[root] = heap[root], heap[2 * root + 2]
            adjuste_tree(heap, 2 * root + 2)
    # 无右子节点 且 （左节点 > 根）
    if  2*root+2 <= len(heap) and (heap[2*root+1] > heap[root]):
        heap[2 * root + 1],heap[root] = heap[root],heap[2 * root + 1]
        adjuste_tree(heap, 2 * root + 1)

def Heap_sort(list):
    #1,建堆,以找出最大值
    #第一个非叶子节点为len/2-1
    n = int(len(list) / 2 - 1)
    for non_leaf in range(n,-1,-1):  #根节点序号为0时也要排序
        #若节点小于他的子节点。
        adjuste_tree(list,non_leaf)

if __name__ == '__main__':
    list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    soted_heap_list = []

    #2,取出根再调整堆
    #3,重复2直到只剩下一个数
    while(len(list)):
        Heap_sort(list)
        soted_heap_list.append(list.pop(0))
    print(soted_heap_list)