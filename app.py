from flask import Flask, jsonify, request
from models import db, Task
from schemas import ma, task_schema, tasks_schema

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) #connecting base from models.py 

with app.app_context():
    db.create_all()

ma.init_app(app)

tasks = [
    {"id": 1, "title": "pracuj 8h", "done": False},
    {"id": 2, "title": "zainstaluj docker", "done": False},
    {"id": 3, "title": "nagraj wokal", "done": False}
    ]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)
def create_task():
    data = request.get_json()
    new_task = Task(title=data["title"], done=False)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "zadanie dodane"}), 201

if __name__ == '__main__':
    app.run(debug=True)



