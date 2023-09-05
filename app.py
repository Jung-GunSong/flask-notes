import os

from flask import Flask, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import UserRegForm, UserLoginForm, CRSRFProtectForm

from models import connect_db, User, db

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///notes_app")

connect_db(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def redirect_home_page():
    """Shows list of all pets"""

    return redirect("/register")


@app.route("/register", methods=["GET", "POST"])
def register_user():
    """Process the register form, adding a new user and goes to the user
    detail page"""

    form = UserRegForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        user = User.register_user(username, password, first_name, last_name, email)

        db.session.add(user)
        db.session.commit()

        return redirect(f"/users/{username}")

    else:
        return render_template('register_user.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login_user():
    """Attemps to log a user in using input username + password"""

    form = UserLoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate_login(username, password)

        if user:

            session["user_username"] = user.username

            db.session.add(user)
            db.session.commit()

            return redirect(f"/users/{username}")

    else:
        return render_template('login_form.html', form=form)

@app.get('/users/<username>')
def view_user(username):

    user = User.query.get_or_404(username)
    form = CRSRFProtectForm()

    return render_template("user_profile.html", user=user, form=form)

@app.post('/logout')
def logout_user():

    form = CRSRFProtectForm()

    if form.validate_on_submit():
        session.pop("user_username", None)

    return redirect("/")
