from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return 'This is the home page'

    

@app.route('/home')
def greet():
    response = make_response() 
    response.status_code = 201
    response.headers['content type'] = 'python/text'
    return response

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