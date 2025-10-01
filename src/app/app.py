from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder = 'templates')


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/second')
def second():
    return 'this is the second page'

@app.route('/home')
def home():
    return redirect(url_for('/'))

if __name__ == '__main__':
    app.run(debug=True)