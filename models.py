from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash



# this is now in app.py file
"""app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
"""
db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    done = db.Column(db.Boolean, default = False)

class User(db.Model)
    id = db.Column(db.Integer, primary_key = True)
    email = db.Colummn(db.String(28),  unique = True, nullable = False)
    password = db.Column(db.String(30), nullable = False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        self.password = check_password_hash(self.password, password)
"""with app.app_context():
    db.create_all()"""
