# flaskblog

## Purpose
This app was created by following a tutorial series on the Flask framework. I wanted to get a quick but comprehensive start into the framework and a starting point for further explorations. 

The app provides a basic multi user blog functionality, which includes:
- user management with registration, password reset, login/logout
- a main page for all posts, ordered by date
- pages for posts by specific users
- user profiles, with name and image editing features

## Understanding The App

### Database:

A SQLite databse is used as the backbone for the web app and managed with the SQLAlchemy framework. There are only two tables used, 'User' and 'Post', which are connected by a one-to-many relationship. The specific rows, can be seen in the following diagram.

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/erdia.png?raw=true)


