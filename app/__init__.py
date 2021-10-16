import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://oleg:oleg@localhost/test'
# app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'test@gmail.com'  # введите свой адрес электронной почты здесь
app.config['MAIL_DEFAULT_SENDER'] = 'test@gmail.com'  # и здесь
app.config['MAIL_PASSWORD'] = 'password'  # введите пароль

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

# добавляем возможность создания миграций с помощью Alembic
migrate = Migrate(app,  db)
# добавляем возможность рассылки писем
mail = Mail(app)
# подключаем аутентификацию пользователей
login_manager = LoginManager(app)
login_manager.login_view = 'login'
from .veiws import *
