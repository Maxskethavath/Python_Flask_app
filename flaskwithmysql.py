from flask import Flask
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MySQL_HOST']="local"
app.config['MySQL_PASSWORD']="local"
app.config['MySQL_USER']="root"
app.config['MySQL_DB']="local"
