'''
求最大子数组问题.
时间复杂度：O(n)
'''
def find_max_array(list):
    l = 0
    r = len(list)
    if l==r:
        return list
    else:
        mid = (l+r)//2
        l_list = list[l:mid]
        r_list = list[mid:r]

        lmax = 0
        lsum = 0
        xuhao1 = []
        for i in range(mid-1,l-1,-1):
            lsum = lsum + l_list[i]
            if lsum > lmax:
                lmax = lsum
                xuhao1.append(i)
        if len(xuhao1) == 0:
            pass
        else:
            l_min_xuhao = min(xuhao1)
            l_max_xuhao = max(xuhao1)
        print("xuhao1:",xuhao1,l_min_xuhao,l_max_xuhao)

        rmax = 0
        rsum = 0
        xuhao2 = []
        for j in range(mid,r):
            rsum = rsum + list[j]
            if rsum > rmax:
                rmax = rsum
                xuhao2.append(j)
        if len(xuhao2) == 0:
            pass
        else:
            r_min_xuhao = min(xuhao2)
            r_max_xuhao = max(xuhao2)
        print("xuhao2:", xuhao2, r_min_xuhao, r_max_xuhao)

        sum_l_r = lmax + rmax
        print("sum_l_r:",sum_l_r)

        if sum_l_r > lmax and sum_l_r > rmax:
            print(list[l_min_xuhao:r_max_xuhao+1])
        else:
            if lmax > rmax:
                print(list[l_min_xuhao:l_max_xuhao])
            else:
                print(list[r_min_xuhao:r_max_xuhao])

list =[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

find_max_array(list)
'''
[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]  -->  [18, 20, -7, 12]
list = [-2,2,-3,4,-1,2,1,-5,3]   -->  [4,−1,2,1]
'''