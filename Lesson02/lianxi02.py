#去掉列表中重复的数字，打印出不带重复数据的列表

data = [1,3,5,9,0,3,5,2,6,7,2,4,6,8,7,4,1,0,9]
result =[]
#break只退出内层循环
for i  in data:
    for j in result:
        if i ==j:
            break
    else:
        result.append(i)
print(result)

#方法二
for i in data:
    if i in result:
        continue

    result.append(i)
print(result)




