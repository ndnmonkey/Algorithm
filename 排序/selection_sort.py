def selection_sort(list):
    new_list = []
    while len(list):
        min = list[0]
        for i in range(0,len(list)):
            if list[i] < min:
                min= list[i]
        new_list.append(min)
        list.remove(min)
    print(new_list)

l = [10,6,7,11,8,3]
selection_sort(l)