from flask_restful import Resource, reqparse
from api.models import BlogModel
from api.schemas import BlogSchema


class BlogListResource(Resource):
    def get(self):
        blogs = BlogModel.objects().all()
        return BlogSchema(many=True).dump(blogs), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "title", type=str, required=True, help="Title is required"
        )
        parser.add_argument(
            "content", type=str, required=True, help="Content is required"
        )
        args = parser.parse_args()

        blog = BlogModel(title=args["title"], content=args["content"])
        blog.save()

        return BlogSchema().dump(blog), 201

    def put(self):
        return {"message": "Method Not Allowed"}, 405


class BlogSingleResource(Resource):
    def get(self, blog_id):
        blog = BlogModel.objects(id=blog_id).first()
        if blog:
            return BlogSchema().dump(blog), 200
        else:
            return {"message": "Blog not found"}, 404

    def put(self, blog_id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "title", type=str, required=True, help="Title is required"
        )
        parser.add_argument(
            "content", type=str, required=True, help="Content is required"
        )
        args = parser.parse_args()

        blog = BlogModel.objects(pk=blog_id).first()
        if blog:
            blog.title = args["title"]
            blog.content = args["content"]
            blog.save()
            return BlogSchema().dump(blog), 201
        else:
            return {"message": "Blog not found"}, 404

    def delete(self, blog_id):
        blog = BlogModel.objects(pk=blog_id).first()
        if blog:
            blog.delete()
            return {"message": "Blog deleted successfully"}, 204
        else:
            return {"message": "Blog not found"}, 404
