import os
from flask import Flask, send_from_directory, render_template, redirect, request
import subprocess

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/run', methods=["POST"])
def run_code():
    run = subprocess.run(request.data.decode("utf-8"), shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE, encoding="utf-8")
    return run.stdout, run.stderr


@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')

if __name__ == "__main__":
    app.run(port=port)
