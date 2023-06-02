def test_home_page(test_client):
    '''
    GIVEN an app configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    '''
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Flask Blog" in response.data
    assert b"Home Page!" in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data


def test_home_page_post(test_client):
    '''
    GIVEN a app configured for testing
    WHEN the '/' page is posted to (POST)
    THEN check that the '405' status code is returned'
    '''
    response = test_client.post('/')
    assert response.status_code == 405
    assert b"Flask Blog" not in response.data
    assert b"Home Page!" not in response.data


def test_about_page(test_client):
    '''
    GIVEN a app configured for testing
    WHEN the '/about' page is requested (GET)
    THEN check that the response is valid
    '''
    response = test_client.get('/about')
    assert response.status_code == 200
    assert b"About Page!" in response.data


def test_about_page_post(test_client):
    '''
    GIVEN a app configured for testing
    WHEN the '/about' page is posted to (POST)
    THEN check that the '405' status code is returned'
    '''
    response = test_client.post('/about')
    assert response.status_code == 405
    assert b"About Page!" not in response.data
