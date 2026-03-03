a=int(input("daxil et:  "))
def ters(a):
    a_local=a
    s=0
    while a_local>0:
          q=a_local%10
          a_local=a_local//10
          s=q*10=s
    return s
print(ters(a))
