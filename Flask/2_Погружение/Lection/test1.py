from pathlib import Path, PurePath

from flask import Flask, request, render_template
from markupsafe import escape
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello world'


# @app.route('/<path:file>/')
# def get_file(file):
#     return f'Ваш файл: {escape(file)}'


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл загружен на сервер'
    return render_template('/upload_test.html')


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url
    }
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)

