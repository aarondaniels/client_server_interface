#add driver
import mysql.connector


#add connection string
cnx = mysql.connector.connect(user = 'root',
    password='#######',
    host='localhost', #localhost or 127.0.0.1
    database = '#######',
    auth_plugin='mysql_native_password' #type of authentication
    )

#Cursor class allows python code to execute SQL commands in a database session 
cursor = cnx.cursor()
query = ("SELECT * FROM drive_data")
cursor.execute(query)

#iterate through all items in table and write to terminal
for row in cursor.fetchall():
    print(row)

#clean up - close cursor and connection
cursor.close()
cnx.close()