from app import app, db
from flask import redirect, url_for, render_template, flash, make_response, request, session
from forms import ContactForm
from models import Feedback


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
        feedback = Feedback(name=name, email=email, message=message)
        db.session.add(feedback)
        db.session.commit()
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
    ...
