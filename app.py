from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from marshmallow import ValidationError
from models import db, Task, User
from schemas import ma, task_schema, tasks_schema, register_schema, login_schema, LoginSchema
from flask_jwt_extended import jwt_required, get_jwt_identity


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

        return jsonify({"message": ""}), 201


    except Exception as e:
        return jsonify({"error": "server error", "details": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        schema = LoginSchema()

        errors = schema.load(data)

        """if errors:
            return jsonify({"error": errors}), 400"""
        user = schema.context["user"]

        access_token = create_access_token(identity = str(user.id))

        return jsonify({"access_token": access_token}), 200
        
    except Exception as e:
        return jsonify({"error": "server error", "details": str(e)}), 500
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 401    

#tasks
@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    current_user_id = get_jwt_identity()
    user_tasks = Task.query.filter_by(user_id = current_user_id).all()
    print("logged in user: ", current_user_id)
    return jsonify(tasks_schema.dump(user_tasks)), 200

@app.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    try:
        current_user_id = get_jwt_identity()
        data = request.get_json()

        errors = task_schema.validate(data)
        if errors:
            return jsonify({"error": errors}), 400
        
        new_task = Task(title = data["title"], done = False, user_id=int(current_user_id))
        db.session.add(new_task)
        db.session.commit()

        return jsonify(task_schema.dump(new_task)), 201
    except Exception as e:
        return jsonify({"error": "server error", "details": str(e)}), 500
@app.route('/tasks/<int:task_id>', methods = ['DELETE'])
@jwt_required()
def delete_task(task_id):
    try:
        current_user_id = int(get_jwt_identity())
        task = Task.query.filter_by(id = task_id, user_id = current_user_id).first()

        if not task:
            return jsonify({"error": "Task not found, 404"}), 404
        
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "task deleted"}), 200
    
    except Exception as e:
        return jsonify({"message": "serwer error", "details": str(e)}), 500
        
#START

if __name__ == '__main__':
    app.run(debug=True)



