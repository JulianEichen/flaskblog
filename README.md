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
- pytest: testing framework

### Structure

The package [structure](https://julianeichen.github.io/flaskblogtree) is chosen according to the flask specifications. In the first layer we can see *run.py* and the *instance*, *flaskblog* and *tests* subdirectories. Instance contains the database, described below. tests contains all the tests and related files, divided into functional and unit tests. The run file creates and runs an app object. Configuration of said object is specified in the *init.py* and *config.py* files in the first layer of the flaskblog subdirectory. In this layer we also have a *models.py* file to define the *User* and *Post* classes, which describe most of the persistent data. The rest of the layer is made up of 3 kinds of subdirectories. The first one is *templates*, which contains all the html templates. *static* contains static data like the *main.css* file and persistent data that isn't directly handled by the database, like the profile pictures in our case. The last type is made up of *errors*, *main*, *posts* and *users*. These directories are named after the part of the business logic they are related to. Each directory contains an empty *init.py* according to generic Python package structure and also a *routes.py* file (or *handlers.py* in the case of errors). Here a specific *Blueprint* object gets initialized and equipped with route functions to handle whatever request can be made during the apps existence. The Blueprint class is part of the flask framework and used to extend instances of app objects (see the main init file in layer 2).

README.md, Testing.md and the *pictures* directory are for demonstration purpose and not directly related to the actual code. 

### Database

A SQLite database is used to handle the User and Post models. It's made up of the following tables, which are related by a one-to-many relationship (One user -> many posts):

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/erdia.png?raw=true)

### Usage
#### Running The App Locally

Assuming we are using Linux and Python 3.10+ is installed, we can use the following commands in a terminal to download the repository, install the dependencies. 

```
git clone https://github.com/JulianEichen/flaskblog
cd flaskblog
pip install -r requirements.txt
```

Now we have to set up the database uri und key. We can either set them directly in the config file or use environment variables. 
Set up of flask_mail is slightly more complicated. In it's current state, the app is set up to be used with a gmail account. The username and password are stored as environmental variables, but could also be set in the config file. <br>
Note that the gmail account has to be [set up](https://www.youtube.com/watch?v=Jp9B0rY6Fxk) for this use.

When we are done setting up the database and mail configurations, we can 
```
python3 run.py
```
and access the app in a browser under http://localhost:5000/
### Navigation

Navigation happens primarily through the navigation bar, which comes in specific shapes for a logged in or logged out user:

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_navbar_in.png?raw=true)

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_navbar_out.png?raw=true)

### Home Page
The most important page is the home page, where all the posts are show, ordered from most recent to oldest. The amount of posts are set to 5 posts per page and a user can browse through the pages with buttons at the bottom of the home page. 

**Top of the page:**

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_home1.png?raw=true)

**Bottom of the page:**

![alt text](https://github.com/JulianEichen/flaskblog/blob/main/pictures/fl_home2.png?raw=true)

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

## Testing

We use *pytest* to provide functional and unit testing. It is advisable to run pytest through the python interpreter: 

```
python3 -m pytest
```

Pytest will then search the project directory for files which start with the word 'test' and within those files find all functions which start with the word test. It will also run the *conftest.py* file which defines fixtures and other test setup related code. 

### Testing Setup

With *pytest* we'll have most of the setup done in *conftest.py*, such as creating a testing client and database. The client is created through the use of the *create_app(Config)* facotry with a specific testing config file. One important detail is that, since some of the pages are only visible to logged in users, we need to set WTF_CSRF_ENABLED=False.
