import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager

# создание экземпляра приложения
app = Flask(__name__)
# для создания переменной среды FLASK_ENV ввести в терминале "export FLASK_ENV=config.ProductionConfig"
# для удаления переменной среды "unset FLASK_ENV"
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopmentConfig')
db = SQLAlchemy(app)
# добавляем возможность создания миграций с помощью Alembic
migrate = Migrate(app,  db)
# добавляем возможность рассылки писем
mail = Mail(app)
# подключаем аутентификацию пользователей
login_manager = LoginManager(app)
login_manager.login_view = 'login'
from .veiws import *
