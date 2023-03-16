import os
import numpy as np
from PIL import Image
from flask import current_app, url_for
from flask_login import current_user

def test_account_page_logged_in(test_client, init_database, login_default_user):
    '''
    GIVEN app configured for testing
    WHEN the '/account' page is requested (GET), when the user is logged in
    THEN check that the response is valid
    '''
    response = test_client.get(url_for('users.account'))
    assert response.status_code == 200
    assert b"Account Info" in response.data

def test_account_page_logged_out(test_client, init_database):
    '''
    GIVEN app configured for testing
    WHEN the '/account' page is requested (GET), when the user is not logged in
    THEN check that the response is valid
    '''
    response = test_client.get(url_for('users.account'),follow_redirects=True)
    assert response.status_code == 200
    assert b"Account Info" not in response.data
    assert b"Please log in to access this page." in response.data

def test_account_page_page_valid_image_update(test_client, init_database, login_default_user):
    '''
    GIVEN app configured for testing
    WHEN the '/account' page is posted to (POST) with a new profile picture file
    THEN check that the response is valid
    '''
    user_img_path=os.path.join(current_app.root_path,'static/profile_pics',current_user.image_file)
    with Image.open(user_img_path) as img:
        old_img=img.resize([128,128]).getdata()

    # upload new file
    new_img_name="funnyfrog.jpg"
    dir = os.path.dirname(__file__)
    new_im_path = os.path.join(dir,new_img_name)

    data={'picture': (open(new_im_path, 'rb'), new_img_name),
          'email': current_user.email,
          'username':current_user.username}
    
    response =test_client.post('/account',
                               data=data,
                               follow_redirects=True)
    
    user_img_path=os.path.join(current_app.root_path,'static/profile_pics',current_user.image_file)
    with Image.open(user_img_path) as img:
        new_img=img.resize([128,128]).getdata()

    assert response.status_code == 200
    assert b"Your account has been updated!" in response.data 
    assert np.bitwise_xor(new_img,old_img).any()

def test_account_page_page_invalid_image_update(test_client, init_database, login_default_user):
    '''
    GIVEN app configured for testing
    WHEN the '/account' page is posted to (POST) with a new profile picture file of an invalid type
    THEN check that the response is valid
    '''
    user_img_path=os.path.join(current_app.root_path,'static/profile_pics',current_user.image_file)
    with Image.open(user_img_path) as img:
        old_img=img.resize([128,128]).getdata()

    # upload new file
    new_img_name="funnyfrog.gif"
    dir = os.path.dirname(__file__)
    new_im_path = os.path.join(dir,new_img_name)

    data={'picture': (open(new_im_path, 'rb'), new_img_name),
          'email': current_user.email,
          'username':current_user.username}
    
    response =test_client.post('/account',
                               data=data,
                               follow_redirects=True)
    
    user_img_path=os.path.join(current_app.root_path,'static/profile_pics',current_user.image_file)
    with Image.open(user_img_path) as img:
        new_img=img.resize([128,128]).getdata()

    assert response.status_code == 200
    assert b"File does not have an approved extension: jpg, png" in response.data 
    assert not(np.bitwise_xor(new_img,old_img).any())    
    
def test_account_page_valid_name_update(test_client, init_database, login_default_user):
    '''
    GIVEN app configured for testing
    WHEN the '/account' page is posted to (POST) with a new valid username
    THEN check that the response is valid
    '''
    old_name=current_user.username

    response = test_client.post('/account',
                                data=dict(email=current_user.email,
                                          username="Newname"),
                                follow_redirects=True)

    assert response.status_code == 200
    assert b"Your account has been updated!" in response.data
    assert current_user.username != old_name

def test_account_page_valid_email_update(test_client, init_database, login_default_user):
    '''
    GIVEN app configured for testing
    WHEN the '/account' page is posted to (POST) with a new valid email
    THEN check that the response is valid
    '''
    old_email=current_user.email

    response = test_client.post('/account',
                                data=dict(email="new@new.com",
                                          username=current_user.username),
                                follow_redirects=True)

    assert response.status_code == 200
    assert b"Your account has been updated!" in response.data
    assert current_user.email != old_email