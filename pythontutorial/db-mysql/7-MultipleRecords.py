import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='pynative',
                             password='pynative@#29')

   records_to_insert = [ (2,'Jon','2018-01-11', 26) ,
                         (3,'Jane','2017-12-11', 27),
                         (4,'Bill','2018-03-23', 26) ]

   sql_insert_query = """ INSERT INTO python_users (id, name, birth_date, age) 
                       VALUES (%s,%s,%s,%s) """

   cursor = connection.cursor(prepared=True)
   #used executemany to insert 3 rows
   result  = cursor.executemany(sql_insert_query, records_to_insert)
   connection.commit()
   print (cursor.rowcount, "Record inserted successfully into python_users table")

except mysql.connector.Error as error :
    print("Failed inserting record into python_users table {}".format(error))

finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("connection is closed")