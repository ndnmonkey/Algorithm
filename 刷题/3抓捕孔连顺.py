def zhua(d,list):
    jieguo = []
    result = []
    for i in range(len(list)):
        for j in range(len(list)):
            for k in range(len(list)):

                if (j > i and k < i) or (j < i and k > i):
                    if (j > i) and (k < i):
                        if list[j] - list[k] <= d:
                            if i != j and j != k and i != k:
                                a = []
                                a.append(list[i])
                                a.append(list[j])
                                a.append(list[k])
                                # print(set(a))
                                jieguo.append(set(a))
                    else:
                        if list[k] - list[j] <= d:
                            if i != j and j != k and i != k:
                                b = []
                                b.append(list[i])
                                b.append(list[j])
                                b.append(list[k])
                                # print(set(b))
                                jieguo.append(set(b))

                else:
                    if k > i:
                        if k > j:
                            if list[k] - list[i] <= d:
                                if i != j and j != k and i != k:
                                    c = []
                                    c.append(list[i])
                                    c.append(list[j])
                                    c.append(list[k])
                                    # print(set(c))
                                    jieguo.append(set(c))

                        else:
                            if list[j] - list[i] <= d:
                                if i != j and j != k and i != k:
                                    e = []
                                    e.append(list[i])
                                    e.append(list[j])
                                    e.append(list[k])
                                    # print(set(e))
                                    jieguo.append(set(e))

                    else:
                        if k > j:
                            if list[i] - list[j] <= d:
                                if i != j and j != k and i != k:
                                    f = []
                                    f.append(list[i])
                                    f.append(list[j])
                                    f.append(list[k])
                                    # print(set(f))
                                    jieguo.append(set(f))
                        else:
                            if list[i] - list[k] <= d:
                                if i != j and j != k and i != k:
                                    g = []
                                    g.append(list[i])
                                    g.append(list[j])
                                    g.append(list[k])
                                    # print(set(g))
                                    jieguo.append(set(g))

            # print(jieguo)
            for m in jieguo:
                if m not in result:
                    result.append(m)
    print(result)

zhua(2,[1,2,3,4,5])