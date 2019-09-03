def jianbie(wuqi,area):
    get_wuqi = sorted(wuqi[area[0]-1:area[1]])
    for i in range(len(get_wuqi)-2):
        # print(get_wuqi[i])
        if get_wuqi[i] + get_wuqi[i + 1] > get_wuqi[i + 2]:
            return True
        return False


print(jianbie([1,10,100,95,101],[3,5]))

def goldbling(wuqi,qujian):
    count = 0
    for i in qujian:
        if jianbie(wuqi,i) == True:
            count = count + 1
    print(count)


wuqi = [1,10,100,95,101]
qujian = [[1,3],[2,4],[2,5],[3,5]]
goldbling(wuqi,qujian)