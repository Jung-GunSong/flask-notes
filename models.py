from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



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


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"