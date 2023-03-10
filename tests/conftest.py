import pytest

from flaskblog import create_app,db
from flaskblog.models import User, Post
from tests.test_config import Config 


@pytest.fixture(scope='module')
def new_user():
    user = User(username='bob',email='bob@bob.bob',password='123')
    return user

@pytest.fixture(scope='module')
def new_post():
    post = Post(title='titletitle', content='contentcontent')
    return post

@pytest.fixture(scope='session')
def app():
    app=create_app(Config)
 
    # other setup can go here
 
    yield app

    # clean up / reset resources here
   

@pytest.fixture(scope='module')
def test_client(app):
    # create client 
    with app.test_client() as testing_client:
        # establish app context
        with app.app_context():
            yield app.test_client()

@pytest.fixture(scope='module')
def init_database(test_client):
    # create database and the database table
    from flaskblog.models import User, Post
    db.create_all()
    
    # insert data
    user1 = User(username='test1user1',email='test1@aol1.com1',password='123')
    user2 = User(username='test2user2',email='test2@aol2.com2',password='123')
    db.session.add(user1)
    db.session.add(user2)

    # commit changes
    db.session.commit()

    yield

    db.drop_all()

@pytest.fixture(scope='module')
def runner(app):
    return app.test_cli_runner()
