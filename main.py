from flask import Flask

app = Flask("My1stApp")

@app.route("/")
def hello():
    return "Hello World!"