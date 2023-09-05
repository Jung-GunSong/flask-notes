from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

class UserRegForm(FlaskForm):
    """Form for registering a user"""

    username = StringField("Username", validators=[InputRequired()])
    password = StringField("Password", validators=[InputRequired()])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])


class UserLoginForm(FlaskForm):
    """Form for registering a user"""

    username = StringField("Username", validators=[InputRequired()])
    password = StringField("Password", validators=[InputRequired()])

class CRSRFProtectForm(FlaskForm):
    """CRSRF protection"""