from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/add-nums/<int:a>/<int:b>/')
def index(a=0, b=0):
    return str(a + b)


if __name__ == '__main__':
    app.run(debug=True)
