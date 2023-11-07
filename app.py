from flask import Flask

app = Flask(__name__) #initialise the instance


@app.route("/") #this is a decorator - a step before a function. the '/' - this routes to the homepage
def home():
    return "<h1>Hello world2!</h1>"
