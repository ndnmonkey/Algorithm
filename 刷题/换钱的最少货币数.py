def minCoins(arr,aim):
    #把dp的初值搞大一些
    dp = [aim*2 for i in range(aim+1)]
    for i in range(aim):
        if i in arr:
            dp[i] = 1

    print(dp)
    #比最小面额小返回0
    if aim < min(arr):
        return 0
    if aim in arr:
        return 1
    else:
        dp_list = []
        for num in arr:
            dp_list.append("dp[i-" + str(num) + "]")
        # print(",".join(dp_list))

        for i in range(max(arr)+1,aim+1):
            dp[i] = min(eval(",".join(dp_list))) + 1
    # print(dp)
    if dp[aim] == aim*2 or dp[aim] == aim*2+1:
        return -1
    else:
        return dp[aim]
print(minCoins([5,3,10],13))