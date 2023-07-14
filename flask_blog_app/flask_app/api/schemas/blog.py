from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Str()


class BlogSchema(Schema):

    id = fields.Str()
    title = fields.Str()
    content = fields.Str()
    author = fields.Nested(UserSchema)
    createdAt = fields.DateTime()
    updatedAt = fields.DateTime()
