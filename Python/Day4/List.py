l1=[]
l2=[1,2,3,4,5]
l3=["Hi","Welcome"]
l4=[1,2.3,4,"hi",(1,2,3)]
l5=[1,[2,4,5,6],"Radha"]


print(l2)
print(l5)
for i in l5:
    print(i)
    
print(l5[1][3])
print(l5[1:3])

for i in range(1,21):
    l1.append(i)
print(l1)

l1=[]
for i in range(1,6):
    no=input("ele : ")
    l1.append(no)
print(l1)

l1=[]
for i in range(1,6):
    no=int(input("ele : "))
    l1.append([no,no*no])
print(l1)

l1=[[2, 4], [5, 25], [8, 64], [4, 16], [56, 3136]]

l1[1][1]=250
print(l1)

l1[1:4]=10,20,30
print(l1)

l1.insert(0,5)
print(l1)

l1.insert(3,15)
print(l1)

l1.insert(-1,150)
print(l1)

l1.insert(-2,250)
print(l1)

del l1[0]
print(l1)

del l1[1:3]
print(l1)


l1=[x for x in range(1,100) ]
print(l1)

l1=[x**2 for x in range(1,100) ]
print(l1)


l1=[(x,x*x,x**3) for x in range(1,11)]
print(l1)


colors=["red","green","blue"]
obj= ["house","car"]

l10=[[cl,ob] for cl in colors for ob in obj]
print(l10)


colors=["red","green","blue"]
obj= ["house","car"]

l10=[(cl,ob) for cl in colors for ob in obj]
print(l10)

l11=[cl.upper() for cl in colors]
print(l11)

l12= [x for x in range(1,21) if x%2==1]
print(l12)

l1=[1,2,3]
l2=[10,20,30]

l3=[] #11,22,33


for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
    
print(l3)

#===========================

l1=[1,2,3]
l2=[3,4,5,6]
print(l1+l2)

print(l1*4)

print(l1==l2)

print(2 in l1)

print([2] in l1)

#----------------------
l3=l1
print(l1)
print(l3)
print(l1 is l3)
print(id(l1))
print(id(l3))

l4=l1[:]
print(l1)
print(l4)
print(l1 is l4)
print(id(l1))
print(id(l4))

#------------------
l1=["abcd","Welcome","Rima","Tina"]
print(len(l1))
print(min(l1))
print(max(l1))
print(list((1,23,45)))
print(list("Welcome"))

#-------------------------------------
l1=["abcd","Welcome","Rima","Tina"]
l2=[1,2,3]

print(l1.extend(l2))
print(l1)

print(l1.pop())
print(l1)

print(l1.pop(1))
print(l1)

print(l1.remove('Rima'))
print(l1)

print(l1.index(2))
print(l1)


l1=[1,2,3,4,1,3,1]
print(l1.count(1))

l1.reverse()
print(l1)

l1.sort()
print(l1)


l1.clear()
print(l1)

l5=l2.copy()
print(l5)

s="Hi welcome to know-It"
l1=s.split()
print(l1)

print("-".join(l1))




