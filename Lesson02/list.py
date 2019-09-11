#coding:utf-8

print(type([123,456,'abc',[999,'def']]))
#dir查看列表的可用操作
print(dir([]))
data = []
#在列表后面追加数据
data.append(123)
data.append('abc')
#按照位置数据插入列表
data.insert(0,['def',999])
#extend和+都是合并列表
data.extend(['xyz',321])
data= data+['000']
#按照列表索引删除元素
data.pop(3)
#清空列表
data.clear()
print(data)
