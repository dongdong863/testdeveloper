#coding:utf-8
#99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        #X乘X=Y，后面带2个空格
        print('{}X{}={}'.format(j,i,j*i),end='  ')
    #循环一次就换行
    print('\n')
    