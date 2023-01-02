class emp:
    pass

class manager(emp):
    pass

e= emp()
m=manager()


print(isinstance(e,emp))
print(isinstance(e,manager))
print(isinstance(m,emp))
print(isinstance(m,manager))

print(issubclass(emp,emp))
print(issubclass(emp,manager))
print(issubclass(manager,emp))
print(issubclass(manager,manager))


#=================================
class emp:
   def __init__(self,eno=0,enm="temp"):
       self.empno=eno
       self.name=enm
   
   def __str__(self):
        return f' Emp : {self.empno}, {self.name}'
       

class manager(emp):
    pass

e= emp()
m=manager()

print(m)


#=================================
class emp:
   def __init__(self,eno=0,enm="temp"):
       self.empno=eno
       self.name=enm
   
   def __str__(self):
        return f' Emp : {self.empno}, {self.name}'
       

class manager(emp):
    def __init__(self,eno,enm,mgr="shrini"):
        #super().__init__(eno,enm)
        emp.__init__(self,eno,enm)
        self.mgr=mgr
   
    def __str__(self):
        return f' Emp : {self.mgr}'  +super().__str__()   

e= emp()
m=manager(12,"Rupesh")

print(m)

#===============================
class emp:
   def __init__(self,eno=0,enm="temp"):
       self.empno=eno
       self.name=enm
   
   def __str__(self):
        return f' Emp : {self.empno}, {self.name}'
       

class manager(emp):
    def __init__(self,eno=0,enm="temp",mgr="shrini"):
        #super().__init__(eno,enm)
        emp.__init__(self,eno,enm)
        self.mgr=mgr
   
    def __str__(self):
        return f' Emp : {self.mgr}'  +super().__str__()   


class salesmanger(manager):
    pass

e= emp()
m=manager(12,"Rupesh")

print(m)

s=salesmanger()
print(s)


print(salesmanger.__mro__)
print(salesmanger.mro())
#===========================================

class A:
    #id=10
    pass
    
class B:
    id=200

class C(A,B):
    #id=300
    pass


c=C()
print(c.id)   
print(C.mro()) 

#------------------


class Temp:
    def __init__(self):
        self.id=100
        self._no=200
        self.__pno=300
        
    def display(self):
       print(self.id,self._no,self.__pno)
       
       
t=Temp()
t.display()  
print(t.id,t._no,t.__pno)     


class ChildTemp(Temp):
    def display(self):
       print(self.id,self._no,self.__pno)
    
    def clsMethod():
        print("In class method")
    
c=ChildTemp()
ChildTemp.clsMethod()
#c.display()       