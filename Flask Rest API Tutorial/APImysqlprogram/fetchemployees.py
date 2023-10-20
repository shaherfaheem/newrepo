import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import flash, request


def fetchListOfEmployees():
 try:
   cursor = mysql_db.cursor(dictionary=True)
  #  conn = mysql.connect()
  #  cursor = conn.cursor(pymysql.cursors.DictCursor)
   cursor.execute("SELECT * FROM employee")
   rows = cursor.fetchall()
   return rows
 except Exception as e:
   print(e)
 finally:
   cursor.close() 
#    conn.close()