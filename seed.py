from app import app
from models import User, db

db.drop_all()
db.create_all()

# For testing database initially
justin = User(username='jsong', password='abcde', first_name="Justin", last_name="Song", email="jsong@gmail.com")
# nemo = Pet(name="Nemo", species="clownfish", age="young", notes="He touched the butt")

db.session.add(justin)
# db.session.add(nemo)
db.session.commit()