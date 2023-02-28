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

The [package structure](https://julianeichen.github.io/flaskblogtree) is chosen according to the flask specifications. In the first layer we can see *run.py* and the *instance* and *flaskblog* subdirectories. Instance contains the database, described below. The run file creates and runs an app object.
Configuration of said object is specified in the *__init__.py* file in the first layer of the flaskblog subdirectory. In this layer we also have a *models.py* file to define the *User* and *Post* classes. The rest of the layer is made up of 3 kinds of subdirectories. The first one is *templates*, which contains all the html templates.






