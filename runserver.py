from app import app, db

# настройка для функции фабрики приложения
# app = create_app(os.getenv('FLASK_ENV') or 'config.DevelopmentConfig')

if __name__ == '__main__':
    db.create_all()
    app.run()
