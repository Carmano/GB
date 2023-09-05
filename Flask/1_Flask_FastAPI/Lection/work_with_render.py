from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index/')
def html_index():
    context = {
        'title': 'Hello world',
        'h1': 'This header',
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
