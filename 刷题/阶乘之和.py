def count_each_char(string):
    res = {}
    for i in string:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    # return res
    list = []
    for i in res.values():
        list.append(i)
    print(max(list))

count_each_char('abbbbaaaaacc')