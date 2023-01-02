s="Hi ' Snehal"
s1='Welcome
 to KnowIt'
s3=''' Hello
hi how r u?
hjkhkjhkj
'''

print(s)
print(s1)
print(s3)

#s[0]='m' #error
s="Welcome Students"
print(s)

#del s[0] #error

#deletion of string
del s
print(s)

print(s1)
print(s3)

for i in s1:
    print(i)
#----------------------------------
s="vaccination"
print(s[5])
print(s[10])
print(s[5:8])

print(s[8:5])
print(s[8:5:-1])
print(s[:])
print(s[2:])
print(s[:8])

print(s[::-1])
print(s[-5:-2])

print(s[:-2])

print(s[-6:])
print(s[::2])
print(s[::-2])

#--------------------------

# + * % [] [:] < > == <= >= ....

s1 ="Corona "
print(s1+s)
s3=s1+s
print(s3)

print(s3*3)

s2="corona "

print(s1<s2)

#-----------------------

#formatting
#1
print("Hi %s, Welcome! aga is %d sal is %.2f"%("Tina",34,6789.90))


#2
print("Dbda students are {},{} and {}".format("smart","clever","Hardworking"))

print("Dbda students are {1},{0} and {2}".format("smart","clever","Hardworking"))
print("Dbda students are {1},{1} and {1}".format("smart","clever","Hardworking"))

print("Dbda students are {s},{c} and {h}".format(s="smart",c="clever",h="Hardworking"))
name="Kishor"
age=45
print(f"{name} is {age} yrs old having salary {1345*56}")

#-----------------------

print("hi \"snehal\", how\'s you?\n Welcome\t back!!")

#---------------------------
nm="Kishor"
print(len(nm))
print(min(nm))
print(max(nm))
no=str(12345)
print(type(no))

#---------------------------
print(str.title.__doc__)

s="WeLcOMe TO KnowIT"
print(s)
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())
print(s.capitalize())
print(s.startswith("We"))
print(s.endswith("IT"))
s1=s[::-1]
print(s1)


print(s.islower())
for i in s:
    print(i.islower())

n="12A345"
print(n.isdigit())
print(n.isalpha())
print(n.isalnum())

s="Welcome"
s1=s.replace('e', 'E')
print(s1)
print(s)
print(s.replace('o', '0000'))


s="Welcome" 
print(s[:4]+s[5:])

s="aeiou"
cnt=0
for i in "welcome":
    if i in s:
        cnt=cnt+1
else:
    print(cnt)










