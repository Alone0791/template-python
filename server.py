import os
from flask import Flask, send_from_directory, render_template, redirect, request
import subprocess
import io
import sys
import traceback

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
    if run.stdout:
        return run.stdout
    else:
        return run.stderr

@app.route('/eval', methods=["POST"])
def proo():
   text = request.data.decode("utf-8")
   if not text:
      return "lol"
   file = io.StringIO()
   sys.stdout = file
   sys.stderr = file
   try:
      exec(text)
   except Exception:
      return traceback.format_exc()
   sys.stdout = sys.__stdout__
   sys.stderr = sys.__stderr__
   return file.getvalue()


@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')

if __name__ == "__main__":
    app.run(port=port)
