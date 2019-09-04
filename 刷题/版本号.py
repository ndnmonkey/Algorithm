import sys
def Func(x,y):
    if int(x[0]) == int(y[0]):
        if int(x[1]) == int(y[1]):
            if len(x) == 2 or len(y) ==2:
                if len(x) > len(y):
                    print(".".join(x))
                else:
                    print(".".join(y))
            else:
                if int(x[2]) > int(y[2]):
                    print(".".join(x))
                else:
                    print(".".join(y))

        else:
            if int(x[1]) > int(y[1]):
                print(".".join(x))
            else:
                print(".".join(y))

    else:
        if int(x[0]) > int(y[0]):
            print(".".join(x))
        else:
            print(".".join(y))


if __name__ == '__main__':

    x = sys.stdin.readline().strip().split(".")
    y = sys.stdin.readline().strip().split(".")
    Func(x,y)
