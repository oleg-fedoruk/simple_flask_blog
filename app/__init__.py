import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://oleg:oleg@localhost/test'
# app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

db = SQLAlchemy(app)
# формат URI для баз данных:  dialect+driver://username:password@host:port/database
# URL базы данных для MySQL с использованием драйвера PyMysql
'mysql+pymysql://root:pass@localhost/my_db'

# URL базы данных для PostgreSQL с использованием psycopg2
'postgresql+psycopg2://root:pass@localhost/my_db'

# URL базы данных для MS-SQL с использованием драйвера pyodbc
'mssql+pyodbc://root:pass@localhost/my_db'

# URL базы данных для Oracle с использованием драйвера cx_Oracle
'oracle+cx_oracle://root:pass@localhost/my_db'
from .veiws import *
