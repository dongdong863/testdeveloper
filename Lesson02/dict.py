print(type({}))

print(dir({}))

data = {'a':1,'b':2}
print(data)
#取出字段所有key,可以循环遍历
print(data.keys())
for key in data.keys():
    print(key)
#取出字典所有value,可以循环遍历
print(data.values())
for value in data.values():
    print(value)
    
#取出字典所有key与value，可以循环遍历
print(data.items())
for key,value in data.items():
    print('key is {0} and value is {1}'.format(key,value))
#print(data['d'])
#如果get函数通过key取不到值，可以添加一个默认值，默认值是None
print(data.get('d',3))
data['a']=16
#设置默认值，有则不变，没有默认值则使用
data.setdefault('d',99)
data.setdefault('b',99)
#合并两个字典
data.updata({'x':999,'y':999,'z':9999})
print(data)