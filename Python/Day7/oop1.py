class emp:
    """this is emp class"""
    pass

e=emp()
print(type(e))
print(id(e))


#1
class emp:
    def __init__(self,eno,name):
        print("Constructor")
        self.eno=eno
        self.name=name
    

e=emp(11,"Ritesh")
print(e.eno,e.name)


#2

class emp:
    def __init__(self,eno,name):
        print("Constructor")
        self.eno=eno
        self.name=name
    

e=emp(11,"Ritesh")
print(e.eno,e.name)
e1=emp(12,"Riya")
e1.bonus=4000

print(e1.eno,e1.name,e1.bonus)
print(e.bonus)


#3

class emp:
    def __init__(self,eno,name):
        print("Constructor")
        self.eno=eno
        self.name=name
    
    def getBonus(self):
        return self.bonus
    
    def setBonus(self,bns):
        self.bonus=bns

e=emp(11,"Ritesh")
print(e.eno,e.name)
e1=emp(12,"Riya")

e1.setBonus(5000)
print(e1.eno,e1.name,e1.bonus)



#4

class emp:
    location="Pune"
    def __init__(self,eno,name):
        print("Constructor")
        self.eno=eno
        self.name=name
    
   

e=emp(11,"Ritesh")
print(e.eno,e.name,e.location)
e1=emp(12,"Riya")
e1.location="Nagpur"
print(e1.eno,e1.name,e1.location)
print(e.eno,e.name,e.location)

#==============================

class emp:
    location="Pune"
    def __init__(self,eno,name):
        print("Constructor")
        self.eno=eno
        self.name=name
    
   
emp.location="Jalna"
e=emp(11,"Ritesh")
print(e.eno,e.name,e.location)
e1=emp(12,"Riya")
print(e1.eno,e1.name,e1.location)

e1.location="Nagpur"
print(e1.eno,e1.name,e1.location)
print(e.eno,e.name,e.location)



#==============================

class emp:
        
    def __init__(self,eno=0,name="temp"):
        print("Constructor")
        self.eno=eno
        self.name=name

e=emp()
e1=emp(10,"Samrusdii")


print(e.eno,e.name)
print(e1.eno,e1.name)


#==============================

class emp:
        
    def __init__(self,eno=0,name="temp"):
        print("Constructor")
        self.eno=eno
        self.name=name
        
    def __del__(self):
        print("In Destructor")

e=emp()
e1=emp(10,"Samrusdii")


print(e.eno,e.name)
print(e1.eno,e1.name)
del e

#==============================

class emp:
        
    def __init__(self,eno=0,name="temp"):
        print("Constructor")
        self.eno=eno
        self.name=name
        
    def display(self):
        print(self.eno, self.name, sep="---")

    def __str__(self):
        return f'Employee {self.eno} and {self.name}'
    
    
e=emp()
e1=emp(10,"Samrusdii")
e.display()
e1.display()



lst=[e,e1]
for i in lst:
    i.display()

lst=[]
for i in range(3):
    id=int(input("id :"))
    name=input("name :")
    lst.append(emp(id,name))

for i in lst:
    i.display()
    
for i in lst:
    print(i)
