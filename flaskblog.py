# save this as app.py
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY']='a343c940d73bd8707d351de0db9c6da6'

posts=[
    {
        'author': 'Julian Eichen',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 4, 2044'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 22, 2044'
    }
]

@app.route('/') # home page
@app.route('/home') 
def home():
    return render_template('home.html', posts=posts)

@app.route('/about') # about page
def about():
    return render_template('about.html',title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title='Login', form=form)



if __name__ == "__main__":
    app.run(debug=True)

