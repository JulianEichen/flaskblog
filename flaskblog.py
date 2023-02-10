# save this as app.py
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/') # home page
@app.route('/home') 
def home():
    name = request.args.get("name", "Home")
    return f'<h1>{escape(name)} Page!</h1>'

@app.route('/about') # home page
def about():
    name = request.args.get("name", "About")
    return f'<h1>{escape(name)} Page!</h1>'


if __name__ == "__main__":
    app.run(debug=True)