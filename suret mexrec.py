suret=int(input("daxil et:  ))
mexrec=int(input("daxil et:  ))
def sadelesdir(suret, mexrec):
    a = suret
    b = mexrec
    while b != 0:
        qaliq = a % b
        a = b
        b = qaliq
    ebob = a
    return (suret//ebob)"/"(mexrec/ebob)
print(sadelesdir(suret,mexrec))
