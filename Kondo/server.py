from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

# ---- Endpoints for serving static assets ----
@app.route('/bootstrap/<path:path>')
def bootstrap_endpoint(path):
    return send_from_directory('static/bootstrap', path)

@app.route('/upload_assets/<path:path>')
def upload_assets_endpoint(path):
    return send_from_directory('static/upload_assets', path)

# ---------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
