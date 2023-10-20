import pymysql
from app import app
from mysql_db import mysql_db
from addemployee import add_Member_Info
from addemployee import home
from deleteemployee import deleteEmployee
from fetchemployees import fetchListOfEmployees
from employeeupdate import update_employee
from errorhandler import page_not_found
from flask import render_template
from flask import flash, request





if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
