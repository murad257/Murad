a=int(input("daxil et: "))
cem=0 
def fac(q):
    h=1
    t=q
    for i in range (1,t+1):
        h=h*i
    return h    
while a>0:
    q=a%10
    cem=cem+fac(q)
    a=a//10
print(cem)
def kva(cem):
    s=0
    t=cem
    while t>0:
        q=t%10
        s=s+q**2
        t=t//10
    print(s)    
    return s      
while cem>1:
    cem=kva(cem)
    print("aye")
if cem==1:
    print("true")
else:
    print("false")        
