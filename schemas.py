from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
from models import User


ma = Marshmallow()

def validate_title(value):
    if not isinstance(value, str) or len(value.strip()) == 0:
        raise ValidationError("title cannot be empty")
    if len(value) > 50:
        raise ValidationError("title cannot exceed 50 characters")

def validate_email(value):
    if not isinstance(value, str) or len(value.strip()) == 0:
        raise ValidationError("email is required")
    if len(value) > 28:
        raise ValidationError("email cannot exceed 28 characters")
    if User.query.filter_by(email = value).first():
        raise ValidationError("You already have an account")
    


class TaskSchema(ma.Schema):
    id = fields.Int(dump_only = True)
    title = fields.Str(required=True, validate=validate_title )
    done = fields.Bool()
class RegisterSchema(ma.Schema):
    email = fields.Str(required=True, validate = validate_email)
    password = fields.Str(required = True)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
register_schema = RegisterSchema()

