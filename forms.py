from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Pet Name", validators=[InputRequired()])

    species = StringField("Species of Pet",
                          validators=[InputRequired(),
                                      AnyOf(['cat', 'dog', 'porcupine'])])

    photo_url = StringField("Photo of Pet, if Available",
                            validators=[URL(require_tld=True), Optional()])
age = SelectField("Age of Pet",
                      choices=[('baby', 'baby'),
                               ('young', 'young'),
                               ('adult', 'adult'),
                               ('senior', 'senior')],
                      validators=[InputRequired(),
                                  AnyOf(['baby', 'young', 'adult', 'senior'])]
                    )

    notes = TextAreaField("Notes/Comments on pet, if any", validators=[Optional()])

    available = BooleanField("Is pet currently available to adopt?",
                             validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing a pet"""

    photo_url = StringField("Photo of Pet, if Available",
                            validators=[URL(require_tld=False), Optional()])

    notes = TextAreaField("Notes/Comments on pet, if any", validators=[Optional()])

    available = BooleanField("Is pet currently available to adopt?",
                             validators=[Optional()])