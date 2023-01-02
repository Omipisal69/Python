# -*- coding: utf-8 -*-

sum1=-5
def add(a,b):
    sum1=a+b
    return sum1


print(add(3,6))
print(sum1)

#----------------------------
sum1=-5
def add(a,b):
    global sum1
    sum1=a+b
    return sum1

print(sum1)
print(add(3,6))
print(sum1)