def repeat(list):
    if len(list) <= 0 or list == None:
        return False
    else:
        for i in range(len(list)):
            while list[i] != i:
                if list[i] == list[list[i]]:
                    return list[i]
                else:
                    temp = list[i]
                    list[i] = list[list[i]]
                    list[temp] = temp

print(repeat([2, 3, 1, 0, 5, 5]))