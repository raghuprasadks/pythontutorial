# -*- coding: utf-8 -*-
import pymysql
# Open database connection
db = pymysql.connect("localhost","root","admin123","pythondb")
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""
cursor.execute(sql)
# disconnect from server
db.close()
