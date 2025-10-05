from flask import Flask, request, make_response, render_template,redirect,url_for

'''
it creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application
'''
app = Flask(__name__)
@app.route('/')  #Slash basically means this becomes my home page.
def welcome():
    return "Welcome to my MLOps application"
@app.route('/hello',methods=['GET','POST'])
def hello():
    #open git bash then paste this curl -X POST http://127.0.0.1:5000/hello (this methods for just POST)
    #if you want "Hello World without -X, then add GET to methods
    if request.method == 'GET':
        return 'You made a GET request to /hello\n'
    elif request.method == 'POST':
        return 'You made a POST request to /hello\n'
    else:
        return 'you will never see this message\n'
    return "Hello World"
@app.route

@app.route('/greet/<name>')
def greet(name):
    #curl -I htpp://127.0.0.1:5000/greet
    return f"Hello {name}", 202  #Simply give way to status code. default is 200 as well
@app.route('/index')
def index():
    response = make_response('<h1>Index Page</h1>')
    response.status_code=202
    response.headers['content-type'] = 'text/html'
    return response
    # return "<h1>This is the index page</h1>"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"<h1>{number1}+{number2} = {number1 + number2}</h1>"

@app.route('/test')
def test():
    myvalue='Tunahan AKYOL'
    myresult = 10+20
    mylist = [10,20,30,40,50]
    return render_template(template_name_or_list='test.html',myvalue=myvalue,myresult=myresult,mylist=mylist)


@app.route('/handle_url_params')
def handle_url_params():
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    return f'{greeting}, {name}'  #if one key is missing, it'll give BadReqestKeyError or None

@app.route('/other')
def other():
    some_text = "Hello Others"
    return render_template('other.html',some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(string):
    return string[::-1]

@app.template_filter('repeat')
def repeat(string,times=2):
    return string*times

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

if __name__ == '__main__':
    app.run(debug=True)  #you don't need to restart with debug = True
