import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import flash, request
from fetchemployees import fetchListOfEmployees


@app.route('/deleteEmployee', methods=['POST'])
def deleteEmployee():
 try:
   cursor = mysql_db.cursor(dictionary=True)
   _id=request.form.get('id')
   print(_id)
   #conn = mysql.connect()
   #cursor = conn.cursor()
   cursor.execute("DELETE FROM employee WHERE id=%s", [_id])
   mysql_db.commit()
   return render_template('view.html',datas=fetchListOfEmployees())
 except Exception as e:
  print(e)
 finally:
  cursor.close() 
#   conn.close()