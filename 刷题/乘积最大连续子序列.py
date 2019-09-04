
import sys
def func(nums):
    nums.append(-1)
    list = []
    sep = [0]

    for i in range(len(nums)):
        if nums[i] < 0:
            if sep[-1] == 0:
                list.append(nums[sep[-1]:i])
            else:
                list.append(nums[sep[-1]+1:i])
            sep.append(i)


    result= []
    for i in list:
        n = 1
        for j in i:
            n = n * j
        result.append(n)


    print(max(result))

if __name__ == '__main__':
    nums = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    func(nums)