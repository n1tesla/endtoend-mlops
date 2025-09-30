from flask import Flask

'''
it creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application
'''
app = Flask(__name__)
@app.route('/')  #Slash basically means this becomes my home page.
def welcome():
    return "Welcome to my MLOps application"

@app.route('/index')
def index():
    return "This is the index page"

if __name__ == '__main__':
    app.run(debug=True)  #you don't need to restart with debug = True
