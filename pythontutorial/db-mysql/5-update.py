import pymysql
from pymysql import MySQLError

# Open database connection
db = pymysql.connect("localhost","root","admin123","pythondb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1  WHERE SEX = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except MySQLError as e:
   # Rollback in case there is any error
   db.rollback()
   print(' error ',e)

# disconnect from server
db.close()