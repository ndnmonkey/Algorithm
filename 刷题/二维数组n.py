'''
二维数组中是否存在数字n
'''
def search(list,n):
    if list == None or n > list[-1][-1]:
        return False
    else:
        result = []
        for i in range(len(list)):
            line = len(list[0])-1
            num = list[i][line]
            if n < num:
                line = line - 1
                num = list[i][line]
            else:
                num = list[i + 1][line]
            result.append(num)
        if n in result:
            return True
        else:
            return False


list = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(search(list,20))