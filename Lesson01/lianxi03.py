#coding：utf-8

salay = float(input("输入要计算的gongzi:"))
level = salay-3500

if level >=80000:
    tax = level*0.45 - 13505
    
if level>=55000:
    tax = level * 0.35 - 5505

elif level >=35000:
    tax = level * 0.3 - 2755

elif level >=9000:
    tax = level * 0.25 - 1005
    
elif level >=4500:
    tax = level * 0.2 - 555
    
elif level >=1500:
    tax = level * 0.1 - 105

elif level >=0:
    tax = level *0.03

else:
    tax = 0

print('你说的的税收是{0}'.format(tax))