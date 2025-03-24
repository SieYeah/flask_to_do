from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    done = db.Column(db.Boolean, default = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    #user = db.relationship("User", backref="tasks")

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(28),  unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)

    def set_password(self, password):
        #print("Hashuję hasło:", password)
        self.password = generate_password_hash(password)
        #print("Zapisuje do self.password:", self.password)

    def check_password(self, password):
        print(f"CHECKING: {password} vs {self.password}")
        return check_password_hash(self.password, password)
