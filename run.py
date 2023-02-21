from flaskblog import create_app # imports from __init__ , since we are working with a package

app=create_app()

if __name__ == "__main__":
    app.run(debug=True)

