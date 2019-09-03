#生成矩阵
# import random
# matrix = [[random.randint(0,10) for i in range(4)] for j in range(4)]
# print(matrix)

matrix = [[1, 3, 5, 9], [8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]]

def minPathsum(matrix):
    if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    else:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[None for j in range(col)] for i in range(row)]
        dp[0][0] = matrix[0][0]
        #铺满列
        for i in range(1,col):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        #铺满行
        for j in range(1,row):
            dp[0][j] = dp[0][j-1] + matrix[0][j]

        #开始动态规划
        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])  + matrix[i][j]
        print(dp,dp[row-1][col-1])
        return dp[row-1][col-1]

minPathsum(matrix)