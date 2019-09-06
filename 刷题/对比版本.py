import sys
input = sys.stdin.readline().split()
version1 = input[0]
version2 = input[1]
if version1<version2:
    print(-1)
elif version1>version2:
    print(1)
else:
    print(0)