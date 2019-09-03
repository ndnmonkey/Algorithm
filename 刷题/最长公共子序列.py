def longest(str1,str2):
    if len(str1) == 0 or len(str2) ==0:
        return -1
    else:
        table = [[None for i in range(len(str1)+1)] for j in range(len(str2)+1)]
        for i in range(len(str1)+1):
            table[0][i] = 0
        for j in range(len(str2) + 1):
            table[j][0] = 0
        #str1+1行，str2+1列。
        for i in range(1,len(str2)+1):
            for j in range(1,len(str1)+1):
                if str2[i-1] == str1[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j],table[i][j-1])
        print("最长公共子序列长度为：",table[-1][-1])
        print(table)

        #输出公共最长子序列


longest("1A2C3D4B56","B1D23CA45B6A")