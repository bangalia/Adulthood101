from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    """A homepage with info and navigation links for your convenience."""
    return render_template('home.html') 

@app.route('/budget')
def compliments():
    """Takes user the the page about budgeting"""
    return render_template('budget.html')

