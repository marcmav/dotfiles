from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    if request.method == 'GET':
        return 'You made a GET request\n'
    elif request.method == 'POST':
        return 'You made a POST request\n'
    else:
        return 'You will never see this message'
    

@app.route('/greet/<name>')
def greet(name):
    return f'Hello {name}', 404

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return f'{a} * {b} = {a*b}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'some parameters are missing'


if __name__ == '__main__':
    app.run(debug=True)