import re
def jsj(list):
    a = list.split('+')

    for i in range(len(a)):
        if "*" in a[i]:
            b = eval(a[i])
            a[i] = str(b)
    return eval('+'.join(a))

jsj('7+3*4*5+2+4-3-1')

def calculate(list):
    for i in list:
        print(jsj(i))

calculate(['7+3*4*5+2+4-3-1','2-3*1'])


while True:
    list = []
    a = input('wenti')
    if a != 'END':
        list.append(a)
    else:
        break
