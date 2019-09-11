#coding:utf-8
print('abc')
print('def')
#一段字符窜"""包起来
print('''这是一段很长的内容
长到一行根本放不下
''')
print(type(str(123)))
data = 'this is a long long long string!'
#切片，字符窜可以用索引的形式存储[],冒号前是开始的位置，冒号后是截止的位置
print(data[10:24])
#冒号前没有写，默认是0
print(data[:24])
#冒号后面没有写，默认是-1
print(data[10:])
print(data[10:-8])
#字母大小写
print('word',capitalize())
print("word",upper())
print('word',lower())

print('hellllllllllllo'.find('lll'))
#将多个字符组合成一个
print('--'.join(['abc','def','big']))
print('hellllllllllllo'.replace('l','&'))