import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import flash, request
from fetchemployees import fetchListOfEmployees


@app.route('/', methods=['GET'])
def add_Member_Info():
   return render_template("view.html",datas=fetchListOfEmployees())
   
@app.route("/add", methods=["POST"])
def home():
 try:
   cursor = mysql_db.cursor(dictionary=True)
  #  _id=request.form.get('id')
   _name=request.form.get('uname')
   _email=request.form.get('email')
   _salary=request.form.get('salary')
   sql = "INSERT INTO employee(uname, email,salary) VALUES(%s, %s , %s)"
   data = (_name, _email,_salary)
  #  conn = mysql.connect()
  #  cursor = conn.cursor()
   cursor.execute(sql, data)
   mysql_db.commit()
   return render_template('view.html',datas=fetchListOfEmployees())
 except Exception as e:
   print(e)
 finally:
   cursor.close() 
  #  conn.close()
