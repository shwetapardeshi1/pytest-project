from flask import Flask
from flask_restful import Api
from connection import DB
from api import BlogListResource, BlogSingleResource


def create_app():
    app = Flask(__name__)
    DB.init_app(app)

    api = Api(app)

    api.add_resource(BlogListResource, "/blog", endpoint="list_blogs")
    api.add_resource(
        BlogSingleResource, "/blog/<string:blog_id>", endpoint="single_blog"
    )
    return app
