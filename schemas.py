from flask_marshmallow import Marshmallow

ma = Marshmallow()

class TaskSchema(ma.Schema): # schemat walidacji
    class Meta:
        fields = ("id", "title", "done")

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
