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
    '''
    app.config.update({
        "TESTING": True,
    })
    '''
    
    # other setup can go here
    from flaskblog.models import User, Post
    with app.app_context():
        db.create_all
        user=User(username='testuser',email='test@aol.com',password='123')
   
        db.session.add(user)
        db.session.commit()

    yield app

    # clean up / reset resources here
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def test_client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
