def knapsack(weight,value,target):
    #初始化二维表，第11个就是10，所以+1处理。
    table = [[None for y in range(target+1)] for x in range(len(weight)+1) ]
    for i in range(len(weight) + 1):
        table[i][0] = 0
    for j in range(target+1):
        table[0][j] = 0

    for i in range(1,len(weight) + 1):  #物品编号
        for j in range(1,target + 1):  #背包容量
            if j >= weight[i-1]:
                table[i][j] = max(table[i-1][j],table[i-1][j-weight[i-1]] + value[i-1])
            else:
                table[i][j] = table[i-1][j]

    print(table)
    print(table[len(weight)][target])

# knapsack([2,3,4,5],[3,4,5,6],8)
knapsack([4,3,10,12,5],[3,9,8,16,20],20)