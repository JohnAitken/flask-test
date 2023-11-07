from flask import Blueprint

#Here are the standard routes for the website

views = Blueprint('views',__name__)

@views.route('/')  #so when on home url this is what runs
def home():
    return "<h1>TEST</h1>"
    