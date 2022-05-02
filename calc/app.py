from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home_page():
    """Simple home page"""
    return 'This is the home page.'

@app.route('/add')
def addition():
    """Returns sub of entered params"""
    a = float(request.args["a"])
    b = float(request.args["b"])

    return str(add(a, b))

@app.route('/sub')
def subtraction():
    """Returns difference of entered params"""
    a = float(request.args["a"])
    b = float(request.args["b"])

    return str(sub(a, b))

@app.route('/mult')
def multiply():
    """Returns product of entered params"""
    a = float(request.args["a"])
    b = float(request.args["b"])

    return str(mult(a, b))

@app.route('/div')
def divide():
    """Returns quotient of entered params"""
    a = float(request.args["a"])
    b = float(request.args["b"])

    return str(div(a, b))

@app.route('/math/<op>')
def math(op):
    a = float(request.args["a"])
    b = float(request.args["b"])

    math_dict = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
    }
    
    return str(math_dict[op](a, b))