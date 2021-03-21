from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    """A homepage with info and navigation links for your convenience."""
    return render_template('home.html') 

@app.route('/budget')
def budget():
    """Takes user the the page about budgeting"""
    return render_template('budget.html')

@app.route('/credit')
def credit():
    """Takes user the the page about credit"""
    return render_template('credit.html')