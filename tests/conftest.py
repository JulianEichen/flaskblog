import pytest

from flaskblog.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(username='bob',email='bob@bob.bob',password='123')
    return user