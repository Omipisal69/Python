n,n1,n2=input("Enter 3 no:").split()
n=int(n)
n1=int(n1)
n2=int(n2)

if n>n1:
    if n>n2:
        print(n, " is bigger")
    else:
        print(n2, "is bigger")
elif n1>n2:
    print(n1 , " is bigger")
else:
    print(n2, "is bigger")




if n> n1 and n>n2:
    print(n, " is bigger")
elif n1>n and n1>n2:
    print(n1, "is bigger")
else:
    print(n2, "is bigger")
    
