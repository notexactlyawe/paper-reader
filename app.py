import os, haven, utils
from flask import Flask, send_from_directory, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/api/v1/concepts', methods=['POST'])
def get_concepts():
    return str(haven.analysis(request.form['url'], False))


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
