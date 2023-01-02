import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
     )
mycursor=mydb.cursor()

mycursor.execute("create database pythontest1")

mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
mycursor.close()
mydb.close()

#-----------------------
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythontest1"
     )
cur=mydb.cursor()
cur.execute("Create table cust(name VARCHAR(255),address VARCHAR(255))")
cur.execute("show tables")

for i in cur:
    print(i)
    
cur.close()    

#----------------------------
cur=mydb.cursor()
sql="Insert into cust(name ,address) values(%s,%s)"
val=("Madhuri","Pune")
cur.execute(sql,val)
mydb.commit()
print(cur.rowcount,"record inserted")

cur.close()    

#----------------------------
cur=mydb.cursor()
sql="Insert into cust(name ,address) values(%s,%s)"
val=[]
for i in range(0,3):
    name=input("enter name")
    city=input("enter add")
    val.append((name,city))

cur.executemany(sql,val)
mydb.commit()
print(cur.rowcount,"record inserted")

cur.close()    
#----------------------------
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythontest1"
     )
cur=mydb.cursor()
sql="Select * from cust"
cur.execute(sql)
#res=cur.fetchall()
#res=cur.fetchone()
res=cur.fetchmany(3)

print(res)
#----------------------------
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythontest1"
     )
cur=mydb.cursor()
sql="Select * from cust where name like 'R%'"
cur.execute(sql)
#res=cur.fetchall()
#res=cur.fetchone()
res=cur.fetchall()

print(res)   
#-------------------------------
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythontest1"
     )
cur=mydb.cursor()
sql="Select * from cust where name=%s"
val=("ram",)
cur.execute(sql,val)
#res=cur.fetchall()
#res=cur.fetchone()
res=cur.fetchmany(3)

print(res)


#-------------------------------
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythontest1"
     )
cur=mydb.cursor()
sql="update cust set name=%s where address=%s"
val=("ram1","kashi")
cur.execute(sql,val)
mydb.commit()
print(cur.rowcount,"records upated")

#-------------------------------
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythontest1"
     )
cur=mydb.cursor()
sql="Delete from cust where address=%s"
val=("kashi",)
cur.execute(sql,val)
mydb.commit()
print(cur.rowcount,"records upated")

#-------------------------------
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythontest1"
     )
cur=mydb.cursor()
sql="drop table cust"
cur.execute(sql)
cur.close()
mydb.close()
