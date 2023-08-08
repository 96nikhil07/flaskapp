### create simple flask app

from flask import Flask,render_template

# create flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/welcome')
def welcome():
    return "Welcome to the second page"

@app.route('/index')
def index():
    return render_template('index.html')


if __name__=='__main__':
    
    app.run(debug=True)
    