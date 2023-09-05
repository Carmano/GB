from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'


@app.route('/Фёдор/')
@app.route("/Fedor/")
@app.route('/Федя/')
def fedor():
    return 'Привет, Федор!'


@app.route('/dog/')
@app.route('/dog/<name>/')
def hello(name='Незнакомец'):
    return f'Привет собака по имени {name.capitalize()}'


@app.route('/file/<path:file>')
def file(file=''):
    return f'Путь до файла {file}'


if __name__ == '__main__':
    app.run()
