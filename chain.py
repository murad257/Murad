a=int(input("daxil et: "))
s=0
def reqem(a):
    s=0
    b=a
    while b>0:
        q=b%10
        b=b//10
        s=s+q
    return s
while a>1:
    s=s+1
    a=a//reqem(a)
print(f"chai {s}")    
