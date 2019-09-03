x = 5

# print(repr(5))
# print(str(5))
# print(eval("5"))

str ='{"name":"mike","age":10,"sex":"男"}'
eval_dic = eval(str)
print(type(eval_dic),"-->",eval_dic,"-->",eval_dic['name'])

repr = repr(str)
print(type(repr),"-->",repr,"-->",repr[0:5])
print(str[0:5])