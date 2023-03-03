# flaskblog
## Purpose

This app was created by following a tutorial series on the *Flask* ramework. I wanted to get a quick but comprehensive start into the framework and a starting point for further explorations.

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

The package [structure](https://julianeichen.github.io/flaskblogtree) is chosen according to the flask specifications. In the first layer we can see *run.py* and the *instance* and *flaskblog* subdirectories. Itance contains the database, described below. The run file creates and runs an app object. Configuration of said object is specified in the *init.py* and *config.py* files in the first layer of the flaskblog subdirectory. In this layer we also have a *models.py* file to define the *User* and *Post* classes, which describe most of the persistent data. The rest of the layer is made up of 3 kinds of subdirectories. The first one is *templates*, which contains all the html templates. *static* contains static data like the *main.css* file and persistent data that isn't directly handled by the database, like the profile pictures in our case. The last type is made up of *errors*, *main*, *posts* and *users*. These directories are named after the part of the business logic they are related to. Each directory contains an empty *init.py* according to generic Python package structure and also a *routes.py* file (or *handlers.py* in the case of errors). Here a specific *Blueprint* object gets initialized and equipped with route functions to handle whatever request can be made during the apps existence. The Blueprint class is part of the flask framework and used to extend instances of app objects (see the main init file in layer 2).
### Database

A SQLite database is used to handle the User and Post models. It's made up of the following tables, which are related by a one-to-many relationship (One user -> many posts):

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/erdia.png?raw=true)

### Usage
#### Running The App Locally

Assuming we are using Linux and Python 3.10+ is installed, we can use the following commands in a terminal to download the repository, install the requirements and run the app.

```
git clone https://github.com/JulianEichen/flaskblog
cd flaskblog
pip install -r requirements.txt
python3 run.py
```

We can then access the app in a browser under http://localhost:5000/
### Navigation

Navigation happens primarily through the navigation bar, which comes in specific shapes for a logged in or logged out user:

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_navbar_in.png?raw=true)

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_navbar_out.png?raw=true)
### Registration, Login And Password Reset

The following forms should be self explanatory. Note that the reset happens via email.

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_register.png?raw=true)

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_login.png?raw=true)

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_reset.png?raw=true)
### Account Page

The Account page shows the user defining information Username and email and also the profile picture. All three can be changed by putting in new data into the form and clicking the Update button or simply uploading a new picture.

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_account.png?raw=true)
### Posts

We have a simple form to create new posts. And a page for each single post, which gives the creater of the post the option to edit the post, if they are logged in.

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_post_new.png?raw=true)

**Logged in as creator of the post:**

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_post_in.png?raw=true)

**General view accessible to every user:**

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_post_out.png?raw=true)
