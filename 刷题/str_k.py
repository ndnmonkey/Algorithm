def topKFrequent(nums, k):
    set1 = set(nums)

#list1-list2剩下list
def cha(list1,list2):
    for i in list1:
        if i in list2:
            list1.remove(i)
    print(list1)
    return list1

l2=[1,3]
l1 = [1,3,1,7,2,4,9,5]
k = 3
topKFrequent(l1, k)
cha(l1,l2)