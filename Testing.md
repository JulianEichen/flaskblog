# Testing

## Unit Tests

### models

- new_user: a new User is created
- new_post: a bew Post is created


## Functional Tests

### main

### posts

### users

- test_register_page: the '/register' page is requested (GET)
- test_valid_registration: the '/register' page is posted to (POST) with valid data
- test_invalid_registration: the '/register' page is posted to (POST) with invalid password confirmation
- test_duplicate_registration: the '/register' page is posted to (POST) using an email address already in use
- test_login_page: the '/login' page is requested (GET)
- test_invalid_login: the '/login' page is posted to (POST) with wrong password
- test_valid_login_logout: the '/login' page is posted to (POST) with valid data, then the '/logout' page is requested (GET)

WIP:

- 



