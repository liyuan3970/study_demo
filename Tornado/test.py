from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, flask!</h1>"

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, %s!</h1>" % name

@app.route('/calc/')
def calc():
    start = "1988"
    today = "2018"
    rel = int(today) - int(start)
    return "<h1>This year is Pingan's %sth anniversary, congratulations!</h1>" % rel

if __name__ == '__main__':
    #app.debug = True
    app.run(host='127.0.0.1', port=8001)
    #app.run()
