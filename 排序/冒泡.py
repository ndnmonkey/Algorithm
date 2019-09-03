def bubble(list):
    #print(list)
    for index in range(1,len(list)):  #比较6趟
        print("       times： %d" %index)
        for index2 in range(len(list)-1,0,-1):
            print("index2 =  %d:" %index2)
            if list[len(list) - index2-1] > list[len(list) - index2]:
                temp = list[len(list) - index2-1]
                list[len(list) - index2 - 1] = list[len(list) - index2]
                list[len(list) - index2] = temp
        print(list)
list = [3, 6, 4, 2, 11, 10, 5,12,1,7,10]
bubble(list)