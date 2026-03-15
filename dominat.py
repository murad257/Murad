a=int(input("daxil et : ")) 
iki=0
c=a
t=1
k=0
while a>0:
    q=a%2
    a=a//2
    iki=iki+t*q
    t=t*10
l=0
while c>0:
    f=c%10
    if f>l:
        l=f
    c=c//10
while iki>0:
    r=iki%10
    if r==1:
        k=k+1
    iki=iki//10
print(l,k)    
if l==k:
    print("dominance")
else:
    print("no")           
