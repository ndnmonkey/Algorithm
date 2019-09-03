def insertion_sort(list):
    for i in range(1,len(list)):
        for j in range(0,i):
            temp = list[i]
            if temp < list[j]:
                list.pop(i)
                list.insert(j,temp)
    return list

l = [3,44,39,5,47,15,36,26,27,2,46,4,19,50,48]
print(insertion_sort(l))