



for i in "python":
    if i=='t':
        pass
    print(i)



'''

for i in "python":
    if i=='t':
        pass
    print(i)



for i in "python":
    if i=='t':
        continue
    print(i)

for i in "python":
    if i=='t':
        break
    print(i)

    
#pattern
row=int(input("Enter row"))
for i in range(1,row+1):
    for j in range(i):
        print("*",end=" ")
    print()




#Verticle
for i in range(1,11):
    for j in range(2,13):
        print(i*j,end=" ")
    print()

#horizontal Table
for i in range(2,13):
    for j in range(1,11):
        print(i*j,end=" ")
    print()


    
for i in range(1,4):
    for j in range(10,15):
        print(i,j)


for i in range(1,50):
    if i%2 ==1:
        print(i)


        
range(1,10)
range(1, 10)
a= range(1,10)
a
range(1, 10)
type(a)
<class 'range'>
list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1,10,2))
[1, 3, 5, 7, 9]
list(range(10,-1,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



no = int(input())
for i in [1,2,3,4,5]:
    if no==i:
        print("Found")
        break
else:
    print("not found")



sum=0
for i in [1,2,3,4,5]:
    sum=sum+i
print(sum)


for i in "Welcome":
    print(i)


for i in [1,2,3,4,5]:
    print(i)



'''
'''
#prog4
mno=145
cnt=0
while cnt<3:
    no =int(input("No : "))
    cnt=cnt+1
    if mno==no:
        print("you win")
        break
    elif no > 150:
        print("bigger no")
    elif no <100:
        print("No is too small")
else:
    print("You lost the game")
    






#prog4
mno=145

while True:
    no =int(input("No : "))
    if mno==no:
        print("you win")
        break
    elif no > 150:
        print("bigger no")
    elif no <100:
        print("No is too small")
        
#Prog3
no=int(input())
fact=1
while no>=1:
    fact=fact*no
    no=no-1
else:
    print(fact)

#Prog2
a= 1
while a<=5:
    print(a)
    a=a+1
else:
    print("Code Execustion completed")

#prog 1
a= 1
while a<=5:
    print(a)
    a=a+1
'''
