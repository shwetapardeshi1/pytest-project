from datetime import datetime

from connection import DB


class BlogModel(DB.Document):
    title = DB.StringField(required=True)
    content = DB.StringField(required=True)
    author = DB.ReferenceField("UserModel", required=False)
    createdAt = DB.DateTimeField(default=datetime.utcnow)
    updatedAt = DB.DateTimeField(default=datetime.utcnow)

    def modify(self, *args, **kwargs):
        """Update timestamp automatically"""

        super(BlogModel, self).modify(
            *args, **kwargs, updatedAt=datetime.utcnow()
        )


class UserModel(DB.Document):
    name = DB.StringField(required=True)
    email = DB.EmailField(required=True)
