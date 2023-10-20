import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import flash, request
from fetchemployees import fetchListOfEmployees

@app.route('/employeeUpdate', methods=['POST'])
def update_employee():
 try:
   cursor = mysql_db.cursor(dictionary=True)
   _id=request.form.get('id')
   _name=request.form.get('uname')
   _email=request.form.get('email')
   _salary=request.form.get('salary')
  
   sql = "UPDATE employee SET uname=%s, email=%s, salary=%s WHERE id=%s"
   data = (_name, _email, _salary, _id,)
  #  conn = mysql.connect()
  #  cursor = conn.cursor()
   cursor.execute(sql, data)
   mysql_db.commit()
   return render_template('view.html',datas=fetchListOfEmployees())
 except Exception as e:
  print(e)
 finally:
  cursor.close() 
#   conn.close()