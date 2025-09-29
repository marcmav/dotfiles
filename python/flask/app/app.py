from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'You made a GET request\n', 200
    elif request.method == 'POST':
        return 'You made a POST request\n', 201
    else:
        return 'You will never see this message', 404
    

@app.route('/<name>')
def greet(name):
    response = make_response() 
    response.status_code = 201
    response.headers['content type'] = 'python/text'
    return response

@app.route('/multiply/<int:a>&<int:b>')
def multiply(a, b):
    return f'{a} * {b} = {a*b}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'some parameters are missing'


if __name__ == '__main__':
    app.run(debug=True)