#bool判断表达式是否成立
print(bool(123==int('123')))
print(bool(False))
age = int(input("请输入你的年龄"))
sex = input("请输入你的性别：")

print(bool(age>50))
print(bool(age >60 or age<70 and sex == 'female'))
if age >70:
    print('大于70')
elif bool(age >60 or age<70 and sex == 'female'):
    print('大于60小于70')
elif age >50:
    print('大于50')
else:
    print('小于50')