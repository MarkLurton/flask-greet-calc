from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home_page():
    """Landing page for app"""
    return "<h1>This is the home page!</h1>"

@app.route('/welcome')
def welcome():
    """welcome page"""
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """welcome home page"""
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """welcome back page"""
    return "welcome back"