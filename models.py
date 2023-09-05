from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt= Bcrypt()


def connect_db(app):
    app.app_context().push()
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User documentation"""
    __tablename__ = "users"

    username = db.Column(
        db.String(20),
        primary_key=True,
        )

    password = db.Column(
        db.String(100),
        nullable=False)


    email = db.Column(
        db.String(100),
        nullable=False,
        unique = True)

    first_name = db.Column(
        db.String(30),
        nullable=False,
        )

    last_name = db.Column(
        db.String(30),
        nullable=False)

    @classmethod
    def register_user(cls, username, password, first_name, last_name, email):

        hash = bcrypt.generate_password_hash(password).decode('utf8')

        user = User(username=username,
                  password=hash,
                  first_name=first_name,
                  last_name=last_name,
                  email=email)

        return user

    @classmethod
    def authenticate_login(cls, username, password):

        user = cls.query.filter_by(username=username).one_or_more()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False