from app import app, db
from models import Role, User
from flask import render_template, flash, redirect, url_for, session
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user


@app.route("/")
@app.route("/index/")
def index():
    roles = Role.query.all()
    print(current_user.user_roles)
    if current_user.is_authenticated:
        return render_template("index.html", roles=roles)
    return redirect(url_for(login.__name__))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(index.__name__))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()

        if user is not None and check_password_hash(
            user.password_hash, form.password.data
        ):
            flash(f"Login {form.login.data}")

            login_user(user=user, remember=True)

            return redirect(url_for("index"))
        flash(f"Такого користувача не існує {form.login.data}")
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for(index.__name__))
    form = RegisterForm()
    if form.validate_on_submit():
        encrypted = generate_password_hash(form.password.data)
        user = User(
            login=form.login.data,
            password_hash=encrypted,
            user_roles=[
                Role.query.filter_by(name="user").first(),
            ],
        )

        db.session.add(user)
        try:
            db.session.commit()
            flash(f"Registered {form.login.data}")
            return redirect(url_for("login"))
        except:
            db.session.rollback()
            flash(f"Такий користувач вже зареєстрований: {form.login.data}!")

    return render_template("register.html", form=form)


@app.errorhandler(404)
def page_not_found(error):
    flash("This page does not exist 404")
    return redirect(url_for(index.__name__))