from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class RegistrationForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()], render_kw={'placeholder': 'Имя'})
    second_name = StringField('second_name', validators=[DataRequired()], render_kw={'placeholder': 'Фамилия'})
    email = StringField('email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Электронный адресс'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Пароль'})
