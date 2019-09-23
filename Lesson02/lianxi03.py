'''
冒泡排序是比较相邻连个大小，如果是升序
前面的大，后面的小，则交换位置

'''
data = [1,3,5,9,0,2,6,7,4,8]

print(data)
#i是按照需要多少次历遍
for i in range(0,len(data)-1):
    #j是控制前后两个比较的变量
    for j in range(0,len(data)-1-i):
        if data[j] >data[i]:
            data[j],data[j+1]=data[j+1],data[j]
    print(data)
print(data)