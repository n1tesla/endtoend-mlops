from flask import Flask

'''
it creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application
'''
app = Flask(__name__)
@app.route('/')  #Slash basically means this becomes my home page.
def welcome():
    return "Welcome to my MLOps application"
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"
@app.route('/index')
def index():
    return "<h1>This is the index page</h1>"



if __name__ == '__main__':
    app.run(debug=True)  #you don't need to restart with debug = True
