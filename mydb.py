import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='TOSHITH@#2005',
     
)

#prepare a cursor Object

cursorObject = dataBase.cursor()

#create the db
cursorObject.execute("CREATE DATABASE dcrm")

print("hey done it!")