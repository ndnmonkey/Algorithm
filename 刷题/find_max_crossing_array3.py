import math

# find max crossing subarray in linear time
def find_max_crossing_subarray(A, low, mid, high):
    max_left, max_right = -1, -1

    # left part of the subarray
    left_sum = float("-Inf")
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if (sum > left_sum):
            left_sum = sum
            max_left = i

    # right part of the subarray
    right_sum = float("-Inf")
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if (sum > right_sum):
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum

# using divide and conquer to solve maximum subarray problem
# time complexity: n*logn
def find_maximum_subarray(A, low, high):
    if (high == low):
        return low, high, A[low]
    else:
        mid = math.floor((low + high) / 2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if (left_sum >= right_sum and left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum and right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

# Python program to find maximum contiguous subarray
# Kadane’s Algorithm
def maxSubArraySum(a, size):
    max_so_far = float("-inf")
    max_ending_here = 0

    for i in range(size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

# using dynamic programming to slove maximum subarray problem
def DP_maximum_subarray(arr):
    t = len(arr)
    MS = [0]*t
    MS[0] = arr[0]

    for i in range(1, t):
        MS[i] = max(MS[i-1]+arr[i], arr[i])

    return MS

def main():
    # example of array A
    A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    # A = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
    # A = [0,-2, 3, 5, -1, 2]
    # A = [-9, -2, -3, -5, -3]
    # A = [1, 2, 3, 4, 5]
    # A = [-2, -3, 4, -1, -2, 1, 5, -3]

    print('using divide and conquer...')
    print("Maximum contiguous sum is",find_maximum_subarray(A, 0, len(A) - 1), '\n')

    print('using Kanade Algorithm...')
    print("Maximum contiguous sum is", maxSubArraySum(A, len(A)), '\n')

    print('using dynamic programming...')
    MS = DP_maximum_subarray(A)
    print("Maximum contiguous sum is", max(MS), '\n')

main()