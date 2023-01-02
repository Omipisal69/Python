import mymath
print(mymath.positive(23))
print(mymath.negative(-23))
print(mymath.even(23))



#=======================================
import mymath as mm
print(mm.positive(23))
print(mm.negative(-23))
print(mm.even(23))


#=======================================
from mymath import even

print(even(23))

print(positive(23))
print(negative(-23))


#==================================

l1=[1,2,3]
l2=[10,20,30]

l3=list(zip(l1,l2))
print(l3)

l4=[]
for i in l3:
    for j in i:
        l4.append(j)
        
print(l4)







