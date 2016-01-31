from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

# ---- Endpoints for serving static assets ----
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

@app.route('/font-awesome/<path:path>')
def send_font_awesome(path):
    return send_from_directory('static/font-awesome', path)
# ---------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
