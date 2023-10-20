import mysql.connector
from datetime import datetime
db = mysql.connector.connect( 
    host = "localhost", 
    user = "root", 
    passwd = "root123", 
    database = "databasetest")

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE databasetest") 

#mycursor.execute("CREATE TABLE Member_Info (MemberID int PRIMARY KEY NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, Age smallint UNSIGNED NOT NULL, Gender ENUM('M','F') NOT NULL, Since VARCHAR(50) NOT NULL, Duration smallint UNSIGNED NOT NULL, Expiration VARCHAR(50))")
#mycursor.execute("INSERT INTO MemberInfo (Name, Age, Gender, Duration, Since, Expiration) VALUES (%s,%s,%s,%s, now(),DATE_ADD(Since, INTERVAL Duration DAY))", ("Sam", 27, "F", 365))

w = input('Enter Name --> ')

x = input('Enter Age --> ')

y = input('Enter Gender --> ')

z = input('Enter Duration --> ')

mycursor.execute("INSERT INTO Member_Info (Name, Age, Gender, Duration, Since, Expiration) VALUES (%s,%s,%s,%s, now(),DATE_ADD(Since, INTERVAL Duration DAY))", (w, x, y, z))



#mycursor.execute("CREATE TABLE Fitness_Training (MemberID int PRIMARY KEY NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, Training_Sessions smallint UNSIGNED NOT NULL, Remaining_Sessions smallint UNSIGNED NOT NULL, Trainings_Attended VARCHAR(50) NOT NULL)")
#mycursor.execute("INSERT INTO Fitness_Training (Name, Training_Sessions, Remaining_Sessions, Trainings_Attended) VALUES (%s,%s,%s,%s)", ("Sam", 144, 125, "Wrestling"))

#mycursor.execute("CREATE TABLE Sales (MemberID int PRIMARY KEY NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, Supplements VARCHAR(100) NOT NULL, Other_Products VARCHAR(100) NOT NULL)")
#mycursor.execute("INSERT INTO Sales (Name, Supplements, Other_Products) VALUES (%s,%s,%s)", ("Sam", "Whey Pro", "Gloves"))



#mycursor.execute("ALTER TABLE MemberInfo ADD COLUMN Expiry VARCHAR(50)")
#mycursor.execute("ALTER TABLE MemberInfo CHANGE Expiry Expiration VARCHAR(50) NOT NULL")


#u = input('Enter Name --> ')
#v = input('Enter MemberID --> ')
#mycursor.execute("UPDATE Member_Info SET Name = %s WHERE MemberID = %s", (u,v))
#mycursor.execute("UPDATE MemberInfo SET Age = %s WHERE MemberID = %s", (31,8))


#mycursor.execute("ALTER TABLE Fitness_Training DROP Name")    
#mycursor.execute("DROP TABLE Member_info")
#mycursor.execute("DELETE FROM Sales WHERE MemberId = 9")

db.commit()

mycursor.execute("SELECT * FROM Member_Info")
#mycursor.execute("SELECT * FROM Fitness_Training")
#mycursor.execute("SELECT * FROM Sales")

#mycursor.execute("SELECT a.MemberID, a.Name, a.Age, b.Trainings_Attended FROM MemberInfo a, Fitness_Training b WHERE a.MemberID = b.MemberID")
#mycursor.execute("SELECT a.MemberID, a.Name, a.Age, b.Trainings_Attended FROM MemberInfo a, Fitness_Training b WHERE a.MemberID = b.MemberID")


#mycursor.execute("SELECT * FROM MemberInfo Where Gender = 'M' ORDER BY MemberID ASC ")
print('Member Info')


for x  in mycursor:
    print(x)
