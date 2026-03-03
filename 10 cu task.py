from math import *
a=int(input("daxil et:  "))
def son(a):
    son_local=a
    return son_local%10
def ilk(a):
    ilk_local=a
    while ilk_local>0:
        if ilk_local%10>0:
            break
        else:
            ilk_local=a_local//10
     return ilk_local     
if sqrt(son(a)+ilk(a))>3:
    print("True")
else:
    print("False")
