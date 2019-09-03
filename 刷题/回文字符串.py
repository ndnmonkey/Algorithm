'''
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
可以删除一个字符
'''
str = "abca"
str_list = list(str)
str_list.reverse()
str1 = ''.join(str_list)

if str == str1:
    print('s')
else:
