a=int(input("daxil et: "))
b=int(input("daxil et: "))
def ebob(x,y):
    while y!=0:
        qaliq=x%y
        x=y
        y=qaliq
    return x
def ekob(x,y):
    return x*y//ebob(x,y)
print(ebob(a,b))
print(ekob(a,b))
    
