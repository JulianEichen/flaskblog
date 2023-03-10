from flask import session, url_for
from flaskblog.models import User

def test_register_page(test_client):
    '''
    GIVEN app configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    '''

    response = test_client.get('/register')
    assert response.status_code == 200
    assert b"Join Today" in response.data
    assert b"Password" in response.data
    assert b"Confirm Password" in response.data

def test_valid_registration(test_client, init_database, app):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_client.post('/register',
                                data=dict(username='new',
                                          email='new@aol.com',
                                          password='123',
                                          confirm_password='123'),
                                follow_redirects=True)
   
    assert response.status_code == 200
    with app.app_context():
        assert User.query.count() == 3
    assert b"Your account has been created" in response.data
    assert b"Log In" in response.data

def test_duplicate_registration(test_client, init_database):
    """
    GIVEN app configured for testing
    WHEN the '/register' page is posted to (POST) using an email address already registered
    THEN check an error message is returned to the user
    """
    response = test_client.post('/register',
                                data=dict(username='dupltest',
                                          email='test1@aol.com',
                                          password='FlaskIsGreat',
                                          confirm_password='FlaskIsGreat'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Email already in use." in response.data

    response = test_client.post('/register',
                                data=dict(username='test1user1',
                                          email='test2000@aol.com',
                                          password='FlaskIsGreat',
                                          confirm_password='FlaskIsGreat'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Username already exists." in response.data

    
def test_login_page(test_client):
    '''
    GIVEN app configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    '''
    
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b"Log In" in response.data
    assert b"email" in response.data
    assert b"Password" in response.data
    assert b"Need An Account?" in response.data

def test_invalid_login(test_client, init_database):
    '''
    GIVEN app configured for testing
    WHEN when '/login' is posted to (POST) with wrong password 
    THEN check that the response is valid
    '''

    response=test_client.post('/login',
                            data=dict(email='test1@aol.com', password='345'),
                             follow_redirects=True)
    assert response.status_code == 200
    print(response.data)
    assert b"Log In" in response.data
    assert b"Login Unsuccessful" in response.data
    assert b"Register" in response.data


def test_valid_login_logout(test_client, init_database):
    '''
    GIVEN app configured for testing
    WHEN when '/login' is posted to (POST)
    THEN check that the response is valid
    '''
    response = test_client.post(url_for('users.login'),
                                data=dict(email='test1@aol.com',
                                          password='123'),
                                follow_redirects=True)
    assert response.status_code == 200

    assert b"Flask Blog" in response.data
    assert b"Home Page!" in response.data
    assert b"Account" in response.data
    assert b"Logout" in response.data

    """
    GIVEN app configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get(url_for('users.logout'), follow_redirects = True)
    assert response.status_code == 200
    assert b"Home Page!" in response.data
    assert b"Register" in response.data
    assert b"Login" in response.data

    
