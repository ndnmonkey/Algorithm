'''
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
'''
import math
def judgesum(n):
    j = int(math.sqrt(n))
    i = 0
    while i <= j:
        sum = i ** 2 + j ** 2
        if n == sum:
            return True
        elif n > sum:
            i = i + 1
        else:
            j = j - 1
    return False

print(judgesum(34))
