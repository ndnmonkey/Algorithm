s = "goodmorninghaha"
s1 = "."
print(s.capitalize())  #首字母大写
print(s.count("g",0,15)) #返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print(s.endswith("d",0,4))#检查字符串是否以 obj 结束，
print(s.find("dm",0,6))
print(s1.join(s))
print(max(s))

print("================")
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
s2 = "abcdedcba"
print(line.split(":",2))
print(line.endswith("e"))
print(s2.find("d"))
print(s2.rfind("d"))