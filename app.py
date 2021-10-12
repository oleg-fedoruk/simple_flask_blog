import datetime
from flask import Flask, redirect, url_for, render_template, flash, make_response, request, session
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm

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


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # здесь логика базы данных
        flash("Message Received", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)


@app.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res


@app.route('/article/', methods=['POST',  'GET'])
def article():
    if request.method == 'POST':
        print(request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60*60*24*15)
        res.headers['location'] = url_for('article')
        return res, 302

    return render_template('article.html')


@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # чтение и обновление данных сессии
    else:
        session['visits'] = 1  # настройка данных сессии
    return "Total visits: {}".format(session.get('visits'))


@app.route('/session/')
def updating_session():
    res = str(session.items())
    cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}
    if 'cart_item' in session:
        session['cart_item']['pineapples'] = '100'
        session.modified = True
    else:
        session['cart_item'] = cart_item
    return res


@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)  # удаление данных о посещениях
    return 'Visits deleted'


if __name__ == '__main__':
    db.create_all()
    app.run()
