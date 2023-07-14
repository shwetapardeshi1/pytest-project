import pytest
from bson import ObjectId


class TestBlogList:
    def test_get(self, client, blog):
        res = client.get("/blog")

        assert res.status_code == 200
        assert res.is_json
        assert res.json[0]["title"] == "Blog 1"

    def test_post(self, client):
        res = client.post(
            "/blog", json={"title": "Test Blog", "content": "Test Content"}
        )

        assert res.status_code == 201
        assert res.is_json
        assert res.json["title"] == "Test Blog"


class TestBlogSingle:
    def test_get_success(self, client, blog):
        blog_id = str(blog.id)
        res = client.get(f"/blog/{blog_id}")

        assert res.status_code == 200
        assert res.is_json

    @pytest.mark.only
    def test_get_not_found(self, client):
        blog_id = str(ObjectId())
        res = client.get(f"/blog/{blog_id}")

        assert res.status_code == 404
        assert res.is_json
        assert res.json["message"] == "Blog not found"

    def test_put_success(self, client, blog):
        blog_id = str(blog.id)
        res = client.put(
            f"/blog/{blog_id}",
            json={"title": "Updated Blog", "content": "Updated Content"},
        )

        assert res.status_code == 201
        assert res.is_json
        assert res.json["title"] == "Updated Blog"

    def test_put_not_found(self, client):
        blog_id = str(ObjectId())
        res = client.put(
            f"/blog/{blog_id}",
            json={"title": "Updated Blog", "content": "Updated Content"},
        )

        assert res.status_code == 404
        assert res.is_json
        assert res.json["message"] == "Blog not found"

    def test_delete_success(self, client, blog):
        blog_id = str(blog.id)
        res = client.delete(f"/blog/{blog_id}")

        assert res.status_code == 204
        assert res.data == b""
