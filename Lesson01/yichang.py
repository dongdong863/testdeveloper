#/coding:utf-8
num = int(input('输入'))

try:
    print(num/0)
except ZeroDivisionError as z:
    print(z)
finally:
    print('最终执行')

