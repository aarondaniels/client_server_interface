#add driver
import mysql.connector

#add connection string
cnx = mysql.connector.connect(user='root',
    password='#########',
    host = 'localhost',
    database = '########',
    auth_plugin = 'mysql_native_password')

first_name = input('Enter actor first name: ')
last_name = input('Enter actor last name: ')

cursor = cnx.cursor()
query = (f"INSERT INTO `actor` VALUES(NULL, '{first_name}', '{last_name}', now())")
cursor.execute(query)

#read content from recent entry
query = ("SELECT * FROM actor")
cursor.execute(query)

#print all the first cell of all the rows
for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()