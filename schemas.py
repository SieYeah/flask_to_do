from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError

ma = Marshmallow()

def validate_title(value):
    if not isinstance(value, str) or len(value.strip()) == 0:
        raise ValidationError("title cannot be empty")
    if len(value) > 50:
        raise ValidationError("title cannot exceed 50 characters")
    


"""class TaskSchema(ma.Schema): # schemat walidacji
    class Meta:
        fields = ("id", "title", "done")"""

class TaskSchema(ma.Schema):
    id = fields.Int(dump_only = True)
    title = fields.Str(required=True, validate=validate_title )
    done = fields.Bool()


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
