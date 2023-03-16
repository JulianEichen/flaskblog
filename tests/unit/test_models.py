def test_new_user(new_user):
    '''
    GIVEN a User model
    WHEN a new User is created
    THEN check email, password and username
    '''
    assert new_user.username == 'bob'
    assert new_user.email == 'bob@bob.bob'
    assert new_user.password == '123'

def test_new_post(new_post):
    '''
    GIVEN a Post model
    WHEN a new Post is created
    THEN check email, password and username
    '''
    assert new_post.title == 'titletitle'
    assert new_post.content == 'contentcontent'

