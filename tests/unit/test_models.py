from flaskblog.models import User, Post 

def test_new_user():
    '''
    GIVEN a User model
    WHEN a new User is created
    THEN check email, password and username
    '''

    t_username='bob'
    t_email='bob@bob.bob'
    t_password='123'
    
    user = User(username=t_username, email=t_email, password=t_password)

    assert user.username == t_username
    assert user.email == t_email
    assert user.password == t_password

def test_new_user_fixture(new_user):
    '''
    GIVEN a User model
    WHEN a new User is created
    THEN check email, password and username
    '''
    assert new_user.username == 'bob'
    assert new_user.email == 'bob@bob.bob'
    assert new_user.password == '123'

def test_new_post_fixture(new_post):
    '''
    GIVEN a Post model
    WHEN a new Post is created
    THEN check email, password and username
    '''
    assert new_post.title == 'titletitle'
    assert new_post.content == 'contentcontent'

