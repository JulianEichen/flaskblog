def test_login_page(test_client):
    '''
    GIVEN app configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    '''
    reponse=test_client.get('/login')
    assert reponse.status_code == 200
    assert b"Log In" in reponse.data
    assert b"email" in reponse.data
    assert b"Password" in reponse.data
    assert b"Need An Account?" in reponse.data

def test_valid_login_logout(test_client, init_database):
    '''
    GIVEN app configured for testing
    WHEN when '/login' is posted to (POST)
    THEN check that the response is valid
    '''
    response=test_client.post('/login',
                             data=dict(email='test1@aol1.com1', password='1234'),
                             follow_redirects=True)
    assert response.status_code == 200
    assert b"Flask Blog" in response.data
    assert b"Home Page!" in response.data
    assert b"Account" in response.data
    assert b"Logout" in response.data