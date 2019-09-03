'''
Given s = "leetcode", return "leotcede".
'''
s = "leetcode"
q = "leotcede"

yuanyin = ['a','e','i','o','u']
dit = {}
s = list(s)
for i in range(len(s)):
    if s[i] in yuanyin:
        dit[i] = s[i]

initlist = list( dit.values())
initlist.reverse()

n = 0
for k in dit:
    dit[k] = initlist[n]
    n = n + 1
print(dit)
print(s)


for i in dit:
    s[i] = dit[i]
print(str(''.join(s)))