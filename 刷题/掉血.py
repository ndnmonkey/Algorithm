import sys
def func(list):
    n = len(list)
    table =[[0 for j in range(n)] for i in range(n)]
    table[0][0] = list[0][0]
    for i in range(1,n):
        table[0][i] =  table[0][i-1] + list[0][i]
    for i in range(1,n):
        table[i][0] =  table[i-1][0] + list[i][0]
    print(table)

    for i in range(1,n):
        for j in range(1,n):
            table[i][j] =min( table[i - 1][j], table[i][j-1]) + list[i][j]

    print(table)
    print(table[n-1][n-1])

func([[5, 5, 7], [6, 7, 8], [2, 2, 4]])

# if __name__ == '__main__':
#     n = int(sys.stdin.readline())
#     list = []
#     for i in range(n):
#         temp =[int(i) for i in sys.stdin.readline().split(",")]
#         list.append(temp)
#     func(list)

