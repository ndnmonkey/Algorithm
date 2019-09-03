'''
Q:一座塔有n层，每层高度不一致，某层高度为X，则爬这层需要时间X。除了爬还能用跳，一次可以跳1或者2层，但必须跳完后必须爬一层才能恢复体力。问到
塔顶的最短时间？
A：
p[i]表示爬到i层最短时间
t[i]表示跳到i层最短时间
1，若爬到第层，则
p[i] = min(p[i-1],t[i-1])+a[i]
2，若跳到第层，则
t[i] =min(p[i-1],p[i-2])
'''
def smallQ(a):
    n = len(a)
    a.insert(0, 0)  #在第一个位置放入0，表示到第0层需要0时间。
    p = [0]   #爬到0层要0时间
    t = [0,0,0]  #跳到0层要0时间，跳到1,2层也要0时间(因为跳不占时间).
    for i in range(1,n+1):
        p.append(min(p[i-1],t[i-1])+a[i])
        if i == 1:  #因为p[i-2]不知道是几
            continue
        if i >= 3:   #因为前三层已经确定了
            t.append(min(p[i-1],p[i-2]))  
    # print(p,t)
    return min(p[i],t[i])


list = [3,5,1,8,4,5,6,2]
print(smallQ(list))