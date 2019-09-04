import sys
def Fun(a):
    b = str(format(a, 'b'))
    count = 0
    for i in b:
        if i == "1":
            count = count + 1
    print(count)

if __name__ == '__main__':
    a = int(sys.stdin.readline())
    Fun(a)