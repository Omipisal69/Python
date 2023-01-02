print(Exception.__subclasses__())


no1=int(input("No1: "))
no2=int(input("No2: "))
res=no1/no2
print(res)

try:
    no1=int(input("No1: "))
    no2=int(input("No2: "))
    res=no1/no2
    print(res)
except:
    print("error occured")



try:
    try:
        no1=int(input("No1: "))
        no2=int(input("No2: "))
    except:
        print("Wrong input")
    try:    
        res=no1/no2
    except:
        print("0 Division error")
    print(res)
except Exception as e:
    print("error occured" ,e)
    
    
try:
    no1=int(input("No1: "))
    no2=int(input("No2: "))
    res=no1/no2
    print(res)
except ValueError as e:
    print("error occured" ,e)
except TypeError as e:
    print("error occured" ,e)
except Exception as e:
    print("error occured" ,e)



try:
    no1=int(input("No1: "))
    no2=int(input("No2: "))
    res=no1/no2
    print(res)
except (ValueError,TypeError,Exception) as e:
    print("error occured" ,e)


try:
    no1=int(input("No1: "))
    no2=int(input("No2: "))
    res=no1/no2
    print(res)
except (ValueError,TypeError,Exception) as e:
    print("error occured" ,e)
else:
    print("Code executed succesfully!!")


try:
    no1=int(input("No1: "))
    no2=int(input("No2: "))
    res=no1/no2
    print(res)
finally:
    print("Anyways I am goining to execute ")


try:
    no1=int(input("No1: "))
    no2=int(input("No2: "))
    res=no1/no2
    print(res)
except (ValueError,TypeError,Exception) as e:
    print("error occured" ,e)
finally:
    print("Anyways I am goining to execute ")


try:
    no1=int(input("No1: "))
    no2=int(input("No2: "))
    res=no1/no2
    print(res)
except (ValueError,TypeError,Exception) as e:
    print("error occured" ,e)
else:
    print("wow ! you r awsome! ")
finally:
    print("Anyways I am goining to execute ")



while(1):
    try:
        no1=int(input("No1: "))
        name=input("Name: ")
    except :
        print("Please enter valid values")
    else:
        print("Welcome !",name, "you are ",no1 ,"yrs old" )
        break

#raise
try:
    age=int(input("age: "))
    if(age<18):
        raise Exception("You are not eligible for votting")
except Exception as e :
    print(e)
else:
    print("You are eligible for votting")
    

age=int(input("age: "))
if(age<18):
    raise ValueError("You are not eligible for votting")



class Notoosmall(Exception):
    pass

class NotooBig(Exception):
    pass

mgno=123
while(1):
    try:
        no=int(input("no: "))
        if no < mgno:
            raise Notoosmall("Number is too small")
        elif no > mgno:
            raise NotooBig("Number is too big")
    except Exception as e:
        print("Pls try again ",e)
    else:
        print("Congragulations you won the game")
        break







