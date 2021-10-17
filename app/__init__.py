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
login_manager.login_view = 'main.login'

# регистрация blueprints
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)


# настройки приложения с вариантом фабрики приложения
# db = SQLAlchemy()
# mail = Mail()
# migrate = Migrate()
# login_manager = LoginManager()
# login_manager.login_view = 'main.login'


# Фабрика приложения
# def create_app(config):
#     app = Flask(__name__)
#     app.config.from_object(config)
#
#     db.init_app(app)
#     mail.init_app(app)
#     migrate.init_app(app, db)
#     login_manager.init_app(app)
#
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)
#
#     return app

# при использовании фабрик приложения пропадает доступ к экземпляру
# приложения в эскизе во время импорта.
# Для получения доступа к экземплярам в эскизе
# нужно использовать прокси current_app из пакета flask
