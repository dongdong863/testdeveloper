#coding:utf-8
year = int(input('输入年：'))
month = int(input('输入月：'))
while True:
    if 1 <= month <=12:
        break
    else:
        print('输入月份错误，请重新输入')
    month = int(input('输入月：'))
day = int(input('输入日：'))

month1,month3,month5,month7,month9,month11=31,31,31,31,31,31
month4,month6,month8,month10,month12=30,30,30,30,30
#四年一润，百年不闰，四百年一润
if year%4 ==0 and year%100!=0 and year%400==0:
    month2 = 29
else:
    month2 = 28
    
if month==1:
    print(day)
if month==2:
    print(month1+day)
if month==3:
    print(month1+month2+day)
if month==4:
    print(month1+month2+month3+day)
if month==5:
    print(month1+month2+month3+month4+day)
if month==6:
    print(month1+month2+month3+month4+month5+day)
if month==7:
    print(month1+month2+month3+month4+month5+month6+day)
if month==8:
    print(month1+month2+month3+month4+month5+month6+month7+day)
if month==9:
    print(month1+month2+month3+month4+month5+month6+month7+month8+day)
if month==10:
    print(month1+month2+month3+month4+month5+month6+month7+month8+month9+day)
if month==11:
    print(month1+month2+month3+month4+month5+month6+month7+month8+month9+month10+day)
if month==12:
    print(month1+month2+month3+month4+month5+month6+month7+month8+month9+month10+month11+day)