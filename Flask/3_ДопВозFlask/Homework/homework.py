from flask import Flask, request, render_template, flash
from flask_wtf.csrf import CSRFProtect
from form import RegistrationForm
from models import db, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    db.session.commit()


@app.route('/registration', methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        first_name = form.first_name.data
        second_name = form.second_name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)

        if User.query.filter((User.first_name == first_name) & (User.second_name == second_name)).first():
            flash('Пользователь с такими данными уже существует')
        else:
            new_user = User(first_name=first_name, second_name=second_name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Пользователь зарегистрирован')

    return render_template('registration.html', form=form)
