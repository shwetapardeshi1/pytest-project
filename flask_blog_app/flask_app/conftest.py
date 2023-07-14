import pytest

from helper import create_app
from mongoengine import connect, disconnect
import mongomock
from tests.factories import BlogFactory


@pytest.fixture(scope="session", autouse=True)
def app():
    app = create_app()
    yield app


@pytest.fixture(autouse=True)
def db():

    mongomock.utcnow()
    disconnect()

    _db = connect(
        db="mongoenginetest",
        host="mongodb://localhost",
        uuidRepresentation="standard",
    )

    yield _db

    _db.drop_database("mongoenginetest")


@pytest.fixture(scope="session", autouse=True)
def client(app):

    with app.test_client() as client:
        yield client


@pytest.fixture
def blog():
    return BlogFactory().save()
