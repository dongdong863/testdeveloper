#coding:utf-8
template = "{0},{1},{2}"
print(template.format('你好','吗','?'))

#查找方法的用法，选中方法右键go to --Declaration
file = open('lesson01.py',encoding='utf-8')
print(file.read())
file.close()

#打开一个文件，将输入的内容保存

data = input('输入文本内容是：')
file = open('data.txt',mode='w',encoding='utf-8')
file.write(data)
file.close()