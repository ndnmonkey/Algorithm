shuru = input()
x = int(shuru.split()[0])
y = int(shuru.split()[1])

n = (y + 1 - x)//3
m = (y + 1 -x )%3
num = n * 2

for i in range(m):
    str1 = ''
    for j in range(1,y-i+1):
        str1 = str1 + str(j)
    str1 = eval(str1)

    if str1%3==0:
        num = num+1
print(num)

