from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from models import db, Task, User
from schemas import ma, task_schema, tasks_schema, register_schema


#CONFIG

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["JWT_SECRET_KEY"] = "bazinga"
jwy =JWTManager(app)


#DATABASE

db.init_app(app) #connecting base from models.py

with app.app_context(): 
    db.create_all()

ma.init_app(app)

tasks = [
    {"id": 1, "title": "pracuj 8h", "done": False},
    {"id": 2, "title": "zainstaluj docker", "done": False},
    {"id": 3, "title": "nagraj wokal", "done": False}
    ]


#ACTUAL APP

#login/regiser

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()

        errors = register_schema.validate(data)
        if errors:
            return jsonify({"error" : errors}), 400
        
        new_user = User(email=data["email"])
        new_user.set_password(data["password"])

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Uzytkownik zarejestrowany"}), 201


    except Exception as e:
        return jsonify({"error": "blad serwa", "details": str(e)}), 500


#tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()

        errors = task_schema.validate(data)
        if errors:
            return jsonify({"error": errors}), 400
        
        new_task = Task(title = data["title"], done = False)
        db.session.add(new_task)
        db.session.commit()

        return jsonify(task_schema.dump(new_task)), 201
    except Exception as e:
        return jsonify({"error": "błąd serwera", "details": str(e)}), 500
 
        
#START

if __name__ == '__main__':
    app.run(debug=True)



