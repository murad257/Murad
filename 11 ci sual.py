a=int(input("daxil et: ))
b=int(input("daxil et: ))
def ebob(a,b):
    a_local=a
    b_local=b
    while b_local!=0:
        qaliq=a%b
        a=b
        b=qaliq
        return a_local
if ebob(a,b)==1:
    print("True")
else:
    print("False:)
