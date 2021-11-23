"""
The flask application package.
"""

import os
import urllib.parse
import pyodbc
import uuid

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#### Collect information for correct application initiation ####

########################################Function required to test app run context (Azure or Debug).###############################################

def getSecret(KeyRef):
    #Function will retrieve required secret keys from secure storage before boot.
    file = open(os.path.dirname(os.path.abspath('secrets.txt')))
    content = file.readlines()
    key = content[KeyRef]
    return key



params = urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hacakthon.database.windows.net,1433;Database=hackathondb;UID=Hackathon;Pwd=HighCode2021;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

#### Final Init####

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Not_a_real_secret' #getSecret(1)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
 
import Postin.views
import Postin.login
