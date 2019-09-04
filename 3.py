def dragon(list):
    row = len(list)
    col = len(list[0])
    dp = [[None for j in range(col)] for i in range(row)]
    dp[0][0] = list[0][0]

    for i in range(1,row):
        dp[i][0] =  dp[i-1][0] +  list[i][0]
    for i in range(1,col):
        dp[0][i] =  dp[0][i-1] +  list[0][i]

    for i in range(1,row):
        for j in range(1,col):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + list[i][j]
    print(dp)

    min_list = []
    for row in dp:
        min_list.append(min(row))
    min_blood = min(min_list)

    #都加到最小数>=1
    step = 1 - min_blood

    for i in range(len(list)):
        for j in range(col):
            dp[i][j] = dp[i][j] + step
    print(dp)
    print(dp[0][0])

list = [
        [-2,-3,3],
        [-5,-10,1],
        [0,30,-5]
       ]
dragon(list)