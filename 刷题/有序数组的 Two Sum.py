'''
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
def twosum(list,target):
    if target > 2 * list[-1] or target < 2 * list[0] or list == None:
        return False
    else:
        i = 0; j = len(list)-1
        while i < j:
            if list[i] + list[j] == target:
                print('序号：:',i,j)
                break
            elif list[i] + list[j] >= target:
                j = j - 1
            else:
                i = i + 1
twosum([2, 7, 11, 15],9)