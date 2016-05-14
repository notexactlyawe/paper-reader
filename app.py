from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
