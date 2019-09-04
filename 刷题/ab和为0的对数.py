import sys
def Fun(list):
    count = 0
    for i in list:
        if (-i) in list:
            count = count + 1
    count = int(count/2)
    print(count)

if __name__ == '__main__':
    list = [int(x) for x in sys.stdin.readline().split(",")]
    print(list)