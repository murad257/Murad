##a=int(input("daxil et:  "))
##while a>0:
##    q=a%10
##    if q<(a%100//10):
##        print("no")
##        exit()
##    a=a//10
##print("yes")        
   

    
##a=int(input("daxil et: "))
##def collatz(a):
##    x=a
##    q=0
##    while x>1:
##        if x%2==0:
##            x=x//2
##            if x>=q:
##                q=x
##        else:
##            x=x*3+1
##            if x>=q:
##                q=x
##        print(x ,end=" ")
##    return q    
##print(f"{collatz(a)} is maximum")


##a=int(input("daxil et: "))
##ters=0
##cem=0
##say=0
##c=0
##while a>0:
##    q=a%10
##    a=a//10
##    ters=ters*10+q
##while ters>0:
##    c=ters%10
##    ters=ters//10
##    cem=cem*10+c
##    say=say+1
##    if cem%say!=0:
##        print("false")
##        exit()
##print("ture")

##a=int(input("daxil et: "))
##for i in range (0,len(str(a)),2):
##    print(int(str(a)[i])*str(a)[i+1],end="")
##    


##a=int(input("daxil et:  "))
##ters=0
##cem=0
##t=0
##y=a
##while a>0:
##    q=a%10
##    a=a//10
##    ters=ters*10+q
##print(ters)    
##if y==ters:
##    while y>0:
##        c=y%2
##        y=y//2
##        cem=cem*10+c
##    iki=cem
##    print(cem)
##    while cem>0:
##        r=cem%10
##        cem=cem//10
##        t=t*10+r
##    if t==iki:
##        print("her ikisi")
##        
##    else:
##        print("tekce 10 luq")
##    
##else:
##    print("hec biri")





    
##a=int(input())
##cem=0
##while a>0:
##        c=a%2
##        a=a//2
##        cem=cem*10+c
##print(cem)        
