import os, haven, utils, sys, summarize, alchemy
from flask import Flask, send_from_directory, render_template, request, url_for
from werkzeug.utils import secure_filename


reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = BASE_DIR + "/static/uploads"


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/api/v1/concepts', methods=['POST'])
def get_concepts():
    data = str(haven.analysis(request.form['url'], False))
    return render_template('learn.html', data=data)


@app.route('/api/v1/extract', methods=['POST'])
def extract_text():
    return str(haven.get_text(request.form['url']))


@app.route('/api/v1/summarize', methods=['POST'])
def summarize_text():
    to_summarize = str(haven.get_text(request.form['url']))
    return summarize.summarize(to_summarize)


@app.route('/api/v1/nouns', methods=['POST'])
def nouns():
    to_noun = str(haven.get_text(request.form['url']))
    return alchemy.extract_nouns(to_noun)


@app.route('/api/v1/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and utils.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return url_for('uploaded_file', filename=filename)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('static/css', path)


@app.route('/img/<path:path>')
def serve_img(path):
    return send_from_directory('static/img', path)


@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('static/js', path)


if __name__ == "__main__":
    app.run(debug=True)
