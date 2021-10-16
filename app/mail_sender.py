from threading import Thread
from flask import render_template
from flask_mail import Message
from app import app, mail


def async_send_mail(app, msg):
    with app.app_context():  # создает контекст приложения
        mail.send(msg)  # отправляет email


def send_mail(subject, recipient, template, **kwargs):
    msg = Message(subject, sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[recipient])
    msg.html = render_template(template, **kwargs)
    thr = Thread(target=async_send_mail, args=[app, msg])  # работа происходит вне функции представления
    thr.start()
    return thr
