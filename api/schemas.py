from marshmallow import Schema, fields

class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    email = fields.Email(required=True)

