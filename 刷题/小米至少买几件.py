'''
预算为n元，买单价分别为  的物品至少可以买几件
'''
import sys
def func(list,budget):
    if budget < min(list):
        print(-1)  #return -1
    else:
        new = sorted(list)

        for i in range(1,len(new)):
            new[i] = new[i-1] + new[i]


        for j in range(len(new)-1):
            if budget >= new[-1]:
                print(len(new))
                break

            if new[j] <= budget and budget < new[j+1] :
                print(j+1)
# func([2,4,5],11)

if __name__ == '__main__':
    zonglei = int(sys.stdin.readline())  #物品数
    list = []
    for i in range(zonglei):
        temp =int(sys.stdin.readline())
        list.append(temp)
    budget = int(sys.stdin.readline())  #预算
    func(list, budget)
