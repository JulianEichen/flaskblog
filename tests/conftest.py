import pytest

from flaskblog import create_app, db, bcrypt
from flaskblog.models import User, Post
from tests.test_config import Config 
from flask.testing import FlaskClient


@pytest.fixture(scope='module')
def new_user():
    user = User(username='bob', email='bob@bob.bob', password='123')
    return user

@pytest.fixture(scope='module')
def new_post():
    post = Post(title='titletitle', content='contentcontent')
    return post


@pytest.fixture(scope='module')
def app():
    app = create_app(Config)
    app.config['WTF_CSRF_ENABLED'] = False

    # other setup can go here
    yield app

    # clean up / reset resources here


@pytest.fixture(scope='module')
def test_client(app):

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def init_database(test_client):
    # create database and the database table
    from flaskblog.models import User, Post
    db.create_all()
    
    # insert data
    hashed_password1 = bcrypt.generate_password_hash('123').decode('utf-8')
    hashed_password2 = bcrypt.generate_password_hash('456').decode('utf-8')
    user1 = User(username='test1user1',email='test1@aol.com',password=hashed_password1)
    user2 = User(username='test2user2',email='test2@aol.com',password=hashed_password2)
    db.session.add(user1)
    db.session.add(user2)

    # commit changes
    db.session.commit()

    yield

    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):

    test_client.post('/login',
                     data=dict(email='test1@aol.com', password='123',remember=False),
                     follow_redirects=True)

    yield

    test_client.get('/logout', follow_redirects=True)


@pytest.fixture(scope='module')
def runner(app):
    return app.test_cli_runner()
