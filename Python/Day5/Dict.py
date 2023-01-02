d={}
print(type(d))

d={1:12,2:34,3:45,2:64,3:75}
print(d)

for i in d:
    print(i)
    
for i in d:
    print(d[i])
    
for i in d.keys():
    print(i)
    
for i in d.values():
    print(i)
    
for i in d.items():
    print(i)
    
for i,j in d.items():
    print(i,j)    
    
for i,j in d.items():
    if(j%2==1):
        print(i,j)
        
d={}
for i in range(0,5):
    key=input("Enter key")
    val=input("Enyer Value")
    d[key]=val
        
d={}
for i in range(0,3):
    key=input("Enter key")
    val=input("Enyer Value")
    d.update({key:val})
    
d["1"]="Deshpande"
print(d)
    
d1={1:23,10:45}
d.update(d1)
print(d)

d3={**d,**d1}
print(d3)

del d3[1]
print(d3)

print(d3.popitem())
print(d3)

print(d3.pop('1'))
print(d3)
 
d3.clear()
print(d3)   

d4={n:n*n for n in range(1,20)}
print(d4)
    
l1=[1,2,3,4,5]
l2=[10,20,30,40,50]

d=dict(zip(l1,l2))
print(d)
 
d1=d
   
print(d1==d)  

print(len(d))
print(min(d))
print(max(d))
    
    
print(max(d.values()))        
        
        
        
print(d)

no=int(input("key: "))
if no in d:
    print(d[no])


no=int(input("key: "))
print(d.get(no))


l1=['a','b','c','d']
d=dict.fromkeys(l1)
print(d)

l1=['a','b','c','d']
d=dict.fromkeys(l1,10)
print(d)

s=d.setdefault("d","add me")
print(s)
print(d)

s=d.setdefault("p","add me")
print(s)
print(d)


d4={1: 1, 4: 4, 3: 9, 9: 16, 5: 25}
print(d4)

lst=sorted(d4)

for i in lst:
    print(i,d4[i])


        
        
        