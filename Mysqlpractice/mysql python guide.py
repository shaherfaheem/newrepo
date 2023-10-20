import mysql.connector

#next is to connect or login to your mysql
db = mysql.connector.connect( 
    host = "localhost", 
    user = "root", 
    passwd = "inputyourpassword", 
    database = "databasetest") #use this database command once your database is already created or is already existing

mycursor = db.cursor() #use this to navigate through your mysql

mycursor.execute("CREATE DATABASE yourdatabasename") #use this to create database

mycursor.execute("CREATE TABLE inserttablename (column1 VARCHAR(50), column2 smallint UNSIGNED, column3 int PRIMARY KEY AUTO_INCREMENT)")
    #use this to create table name and columns

mycursor.execute("INSERT INTO yourtablename (column1, column2) VALUES (%s,%s)", ("column1dataname", "column2dataname"))
#use this to insert data into table columns

db.commit()
#use this to apply inserted/updated data

mycursor.execute("SELECT * FROM yourtablename")
#use this to select data in table

for x  in mycursor:
    print(x)
 #use this to show data on terminal   