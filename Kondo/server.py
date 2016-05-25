from flask import Flask, render_template, send_from_directory, request, Response
import json, urllib2

app = Flask(__name__)
URL = 'http://104.196.37.250:8080/check'

# ---- Endpoints for serving static assets ----
@app.route('/bootstrap/<path:path>')
def bootstrap_endpoint(path):
    return send_from_directory('static/bootstrap', path)

@app.route('/upload_assets/<path:path>')
def upload_assets_endpoint(path):
    return send_from_directory('static/upload_assets', path)

@app.route('/vexflow/<path:path>')
def vexflow_endpoint(path):
    return send_from_directory('static/vexflow', path)

@app.route('/misc/<path:path>')
def misc_endpoint(path):
    return send_from_directory('static/misc', path)
# ---------------------------------------------

def html_from_errors(errors):
	pass


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
  values = {'chorale': request.files['file_data'].read()}

  data = json.dumps(values)
  jigglypuff_request = urllib2.Request(URL, data, {'Content-Type': 'application/json'})
  response = urllib2.urlopen(jigglypuff_request)

  return json.dumps({"analysis": response.read()})

if __name__ == '__main__':
    app.run()
