from flask_sqlalchemy import SQLAlchemy


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

"""with app.app_context():
    db.create_all()"""
