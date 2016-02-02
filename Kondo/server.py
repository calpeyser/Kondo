from flask import Flask, render_template, send_from_directory, request, Response
import json, requests

app = Flask(__name__)

# ---- Endpoints for serving static assets ----
@app.route('/bootstrap/<path:path>')
def bootstrap_endpoint(path):
    return send_from_directory('static/bootstrap', path)

@app.route('/upload_assets/<path:path>')
def upload_assets_endpoint(path):
    return send_from_directory('static/upload_assets', path)
# ---------------------------------------------

def html_from_errors(errors):
	pass


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
	params = json.dumps({'chorale': request.files['file_data'].read()})
	r = requests.post('http://192.168.99.101:8080/check', params)

	return json.dumps({"analysis": r.json()})


if __name__ == '__main__':
    app.run()
