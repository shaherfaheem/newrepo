import mysql.connector
from datetime import datetime
db = mysql.connector.connect( 
    host = "localhost", 
    user = "root", 
    passwd = "root123", 
    database = "databasetest")

mycursor = db.cursor()


mycursor.execute("CREATE TABLE employee (id bigint(20) PRIMARY KEY NOT NULL AUTO_INCREMENT, uname varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, email varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, salary varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2343")

db.commit()