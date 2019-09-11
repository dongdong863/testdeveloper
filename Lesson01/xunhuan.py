#ecoding:utf-8
#打印0-9的数字
i= 0
while i<10:
    print(i)
    i = i+1
    
#步长输出
for i in range(0,10,2):
    print(i)
    
#输出奇数偶数
count=0
for i in range(0,100):
    if i<40:
        count += 1
        print('第'+str(count)+'次循环跳过')
        continue#跳过当次循环，继续下一次循环，如果下面还有语句也不会执行，直接进入下一轮
        print('去下一轮循环2')
        
    if i%2 == 0:
        print('偶数是:'+str(i))
        
    if i >80:
        break#跳出循环，接着运行循环下外部的语句
    else:
        print('奇数是：'+str(i))
print('跳出来了')

for a in range(0,5):
    if a >2:
        
        continue
    elif a >1:
        break
    print(a)
    