import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import UserRegForm

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

@app.get('/register')
def show_register_user_form():

    form = UserRegForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data



@app.route("/add", methods=["GET", "POST"])
def add_new_pet():
    """Process the add form, adding a new pet and going back to home page"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name,
                  species=species,
                  photo_url=photo_url,
                  age=age, notes=notes,
                  available=available)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template('add_pet.html', form=form)