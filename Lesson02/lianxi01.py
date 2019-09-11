data = 'big_cat_is_a_good_man'
#在python3.x之后，可以在print()之中加end=""来解决，可以自定义结尾字符.end=''不换行
#flag代表下一个单次是否需要大写
flag = False
for i in data:
    if i == data[0]:
        print(i.capitalize(),end='')
    elif i =='_':
        flag =True
        continue
    elif flag == True:
        print(i.capitalize(),end='')
        flag = False
    else:
        print(i,end='')

#方法二
#split函数，以参数分割字符窜

for i in (data.split('_')):
    print(i.capitalize(),end='')