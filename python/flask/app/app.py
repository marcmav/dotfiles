from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"

@app.route('/greet/<name>')
def greet(name):
    return f'Hello {name}'

@app.route('/<int:a>/<int:b>')
def multiply(a, b):
    return f'{a} * {b} = {a*b}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)