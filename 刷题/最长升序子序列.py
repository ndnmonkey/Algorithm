def f(list):
    if len(list) == 1:
        return list
    if len(list) == 0:
        return 0
    else:
        #建立动态规划表
        table = [0 for i in range(len(list))]
        #设表初始值。第一位为1.
        table[0] = 1
        print(list)
        for i in range(1,len(list)):
            list_j = []
            for j in range(i):
                list_j.append(list[j])
            #若当前数比这个数前面的list的最小值还小，那么设置他为1
            if list[i] < min(list_j):
                table[i] = 1
            else:
                #在这个数前面的list中筛选出比这个数小的list，把这些值对应的动态规划表中的最大值+1赋给该位置的动态表。
                min_list = []
                for k in range(i):
                    if list[k] < list[i]:
                        min_list.append(table[k])
                table[i] = max(min_list) + 1
        print(table,max(table))

f([4,1,5,2,6,3])