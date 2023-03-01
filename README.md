# flaskblog

## Purpose
This app was created by following a tutorial series on the *Flask* framework. I wanted to get a quick but comprehensive start into the framework and a starting point for further explorations. 

The app provides a basic multi user blog functionality, which includes:
- user management with registration, password reset, login/logout
- a main page for all posts, ordered by date
- pages for posts by specific users
- user profiles, with name and image editing features

## Understanding The App

### Important Frameworks
- Flask: main framework
- Jinja2: template engine
- Werkzeug: WSGI
- SQLAlchemy: database framework
- itsdangerous: creation and identification of unqiue tokens

### Structure

The [package structure](https://julianeichen.github.io/flaskblogtree) is chosen according to the flask specifications. In the first layer we can see *run.py* and the *instance* and *flaskblog* subdirectories. *instance* contains the database, described below. The *run* file creates and runs an app object.
Configuration of said object is specified in the *__init__.py* and *config.py* files in the first layer of the flaskblog subdirectory. In this layer we also have a *models.py* file to define the *User* and *Post* classes, which describe most of the persistent data. The rest of the layer is made up of 3 kinds of subdirectories. The first one is *templates*, which contains all the html templates. *static* contains static data like the *main.css* file and persistent data that isn't directly handled by the database, like the profile pictures in our case. The last type is made up of *errors*, *main*, *posts* and *users*. These directories are named after the part of the business logic they are related to. Each directory contains an empty *__init__.py* according to generic Python package structure and also a *routes.py* file (or *handlers.py* in the case of *errors*). Here a specific *Blueprint* object gets initialized and equipped with route functions to handle whatever request can be made during the apps existence. The *Blueprint* class is part of the *flask* framework and used to extend instances of app objects (see the main init file in layer 2).

### Database 
A SQLite databse is used to handle the *User* and *Post* models. It's made up of the following tables, which are related by a one-to-many relationship (One user -> many posts):

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/erdia.png?raw=true)








