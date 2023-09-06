from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, Length, Email


class UserRegForm(FlaskForm):
    """Form for registering a user"""
    username = StringField("Username", validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(max=100)])

    first_name = StringField("First Name", validators=[InputRequired(), Length(max=30)])
    last_name = StringField("Last Name", validators=[InputRequired(), Length(max=30)])
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)])


class UserLoginForm(FlaskForm):
    """Form for login for a user"""

    username = StringField("Username", validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(max=100)])

class CRSRFProtectForm(FlaskForm):
    """CRSRF protection"""

class AddNoteForm(FlaskForm):
    """Form for login for a user"""

    title = StringField("Title", validators=[InputRequired(), Length(max=100)])
    content = TextAreaField("Content", validators=[InputRequired()])
    # owner_username = PasswordField("Owner Username", validators=[InputRequired(), Length(max=30)])