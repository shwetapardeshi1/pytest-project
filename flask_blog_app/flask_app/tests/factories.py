from api import BlogModel
from factory import Factory, SubFactory


class BlogFactory(Factory):

    title = "Blog 1"
    content = "This is the first Blog."

    class Meta:
        model = BlogModel
