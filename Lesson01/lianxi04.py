
fenzi=2
fenmu=1
sum=0
#fenzi,fenmu,sum= 2,1,0
for i in range(0,20):
    sum = sum +fenzi/fenmu
    
    tmp=fenzi
    fenzi= fenzi+fenmu
    fenmu=tmp
    #fenzi,femu = fenzi+fenmu,tmp
    
print(sum)