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
"""def create_task():
    data = request.get_json()
    new_task = Task(title=data["title"], done=False)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "zadanie dodane"}), 201"""
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()

        errors = task_schema.validate(data)
        if errors:
            return jsonify({"error": errors}), 400
        

        """if not data:
            return jsonify({"error": "brak JSON"}), 400
        
        if "title" not in data:
            return jsonify({"error": "brak title"}), 400
        if not isinstance(data["title"], str) or len(data["title"].strip()) == 0:
            return jsonify({"error": "title cannot be empty"})
        if len(data["title"]) > 50:
            return jsonify({"error": "title cannot exceed 50 characters"}), 400"""
        
        new_task = Task(title = data["title"], done = False)
        db.session.add(new_task)
        db.session.commit()

        return jsonify(task_schema.dump(new_task)), 201
    except Exception as e:
        return jsonify({"error": "błąd serwera", "details": str(e)}), 500
        
        

if __name__ == '__main__':
    app.run(debug=True)



