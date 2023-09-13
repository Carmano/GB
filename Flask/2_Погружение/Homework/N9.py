# Задание №9
# 📌 Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# 📌 При отправке которой будет создан cookie файл с данными
# пользователя
# 📌 Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# 📌 На странице приветствия должна быть кнопка "Выйти"
# 📌 При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        response = make_response(redirect(url_for('home')))
        response.set_cookie('username', form.get('name'))
        response.set_cookie('email', form.get('email'))
        return response
    return render_template('login.html')


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


@app.route('/home')
def home():
    name = request.cookies.get("username")
    context = {
        'name': name
    }
    return render_template('home.html', **context)


if __name__ == '__main__':
    app.run()

