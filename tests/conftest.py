import pytest

from flaskblog import create_app
from flaskblog.models import User, Post


@pytest.fixture(scope='module')
def new_user():
    user = User(username='bob',email='bob@bob.bob',password='123')
    return user

@pytest.fixture(scope='module')
def new_post():
    post = Post(title='titletitle', content='contentcontent')
    return post

@pytest.fixture()
def app():
    app=create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def test_client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
