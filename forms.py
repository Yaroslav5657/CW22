from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    login = StringField(
        "Логін",
        validators=[
            DataRequired("Логін треба заповнити"),
            Length(min=3, message="Треба щонайменше 3 символи."),
        ],
    )
    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired("Введіть Пароль)"),
        ],
    )
    submit = SubmitField("Тисни")

class RegisterForm(FlaskForm):
    login = StringField(
        "Логін",
        validators=[
            DataRequired("Логін треба заповнити"),
            Length(min=3, message="Треба щонайменше 3 символи."),
        ],
    )
    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired("Введіть Пароль)"),
        ],
    )
    password_confirm = PasswordField(
        "Підтвердіть пароль",
        validators=[
            DataRequired("Введіть Пароль"),
            EqualTo('password')
        ],
    )
    submit = SubmitField("Тисни")

class PostForm(FlaskForm):
    
    header = StringField(
        "Заголовок",
        validators=[
            DataRequired("Текст треба заповнити"),
        ],
    )
    
    body = TextAreaField(
        "Текст",
        validators=[
            DataRequired("Текст треба заповнити"),
            Length(min=10, message="Треба щонайменше 10 символи."),
        ],
    )
    
    submit = SubmitField("Підтвердити")