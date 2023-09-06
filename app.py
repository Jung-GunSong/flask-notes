import os

from flask import Flask, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import UserRegForm, UserLoginForm, CRSRFProtectForm, AddNoteForm
from werkzeug.exceptions import Unauthorized

from models import connect_db, User, db, Note

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///notes_app")

connect_db(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


# TODO: start organizing routes with comments

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

        session["user_username"] = user.username

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
            return redirect(f"/users/{username}")

        flash("Invalid Username/Password Combination Entered")

    return render_template('login_form.html', form=form)


@app.get('/users/<username>')
def view_user(username):

    user = User.query.get_or_404(username)

    if not "user_username" in session or not session["user_username"] == user.username:
        raise Unauthorized()
        # return redirect("/")

    form = CRSRFProtectForm()
    return render_template("user_profile.html", user=user, form=form)


@app.post('/logout')
def logout_user():

    form = CRSRFProtectForm()

    if not form.validate_on_submit():
        raise Unauthorized()

    session.pop("user_username", None)
    return redirect("/")

@app.post('/users/<username>/delete')
def delete_user(username):

    user = User.query.get_or_404(username)

    if not "user_username" in session or not session["user_username"] == user.username:
        raise Unauthorized()

    for note in user.notes:
        db.session.delete(note)
    db.session.commit()

    db.session.delete(user)
    db.session.commit()

    session.pop("user_username", None)
    return redirect("/")

@app.route("/users/<username>/notes/add", methods=["GET", "POST"])
def add_note(username):

    user = User.query.get_or_404(username)

    if not "user_username" in session or not session["user_username"] == user.username:
        raise Unauthorized()

    form = AddNoteForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        owner_username = session["user_username"]

        note = Note(title=title, content=content, owner_username = owner_username)

        db.session.add(note)
        db.session.commit()

        return redirect(f"/users/{username}")

    else:
        return render_template('add_note.html', form=form, user=user)