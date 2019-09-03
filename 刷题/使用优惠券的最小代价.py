# -*- coding:utf-8 -*-
# author = sw

import sys
if __name__ == '__main__':
    '''
    输入：target，券的张数，分别是。
    '''
    inputs = [int(x) for x in sys.stdin.readline().split()]
    # target是消费券的满足金额条件
    target = inputs[0]
    value = inputs[2:]
    N = inputs[1]
    M =  3 * target
    # dp是动态规划数组，dp[x]存储小于x的最接近x的数
    dp = [ 0 for i in range(M+1)]

    for i in range(N):
        for j in range(value[i],M + 1 )[::-1]:
            tmp = dp[j - value[i]] + value[i]
            if tmp > dp[j] :
                dp[j] = tmp
    # 消费在3倍以内才算
    minn = 3 * target
    res = -1
    for x in dp[target:]:
        if x > target and abs(target - x) < minn:
            minn = abs(target - x)
            res = x
            break
    print(res)
