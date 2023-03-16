# Testing

## Unit Tests

### models

- *test_new_user()*: a new User is created
- *test_new_post()*: a bew Post is created


## Functional Tests

### main

- *test_home_page()*: the '/' page is requested (GET)
- *test_home_page_post()*: the '/' page is posted to (POST)
- *test_about_page()*: the '/about' page is requested (GET)
- *test_about_page_post()*: the '/about' page is posted to (POST)

### posts

### users

**Register, Login And Logout Pages**:
- *test_register_page()*: the '/register' page is requested (GET)
- *test_valid_registration()*: the '/register' page is posted to (POST) with valid data
- *test_invalid_registration()*: the '/register' page is posted to (POST) with invalid password confirmation
- *test_duplicate_registration()*: the '/register' page is posted to (POST) using an email address already in use
- *test_login_page()*: the '/login' page is requested (GET)
- *test_invalid_login()*: the '/login' page is posted to (POST) with wrong password
- *test_valid_login_logout()*: the '/login' page is posted to (POST) with valid data, then the '/logout' page is requested (GET)
- *test_login_already_logged_in()*: the '/login' page is posted to (POST) when the user is already logged in 

**Account Page**:
- *test_account_page_logged_in()*: the '/account' page is requested (GET), when the user is logged in
- *test_account_page_logged_out()*: the '/account' page is requested (GET), when the user is logged out
- *test_account_page_page_valid_image_update()*: the '/account' page is posted to (POST) with a new profile picture file
- *test_account_page_page_invalid_image_update()*: the '/account' page is posted to (POST) with a new profile picture file of an invalid type
- *test_account_page_valid_name_update()*: the '/account' page is posted to (POST) with a new valid username
- *test_account_page_valid_email_update()*: the '/account' page is posted to (POST) with a new valid email
 


