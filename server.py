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

@app.route('eval', methods=["POST"])
def __eval():
    text = request.data.decode("utf-8")
    if not text:
        return "Give code to Execute"
    OLDOUT = sys.stdout
    OLDER = sys.stderr
    NEWOUT = sys.stdout = io.StringIO()
    NEWER = sys.stderr = io.StringIO()
    stdout, stderr, exc, = None, None, None
    try:
	value = await aexec(args, event)
    except Exception:
        value = None
	exc = traceback.format_exc()
    NEWOUTT = NEWOUT.getvalue()
    NEWERR = NEWER.getvalue()
    sys.stdout = OLDOUT
    sys.stderr = OLDER
    edit = ''
    if exc:
	edit = exc
    elif NEWOUTT:
	edit = NEWOUTT
    elif NEWERR:
	edit = NEWERR
    else:
	edit = '<pre><code>SUCKSEXX</code></pre>'
    #	final_output = "**EVAL : ♡**\n "
    final_output = f"<pre><code>{args}</code></pre>"
#	final_output += "**OUTPUT: ☆**\n"
    final_output += f"<pre><code>{edit.strip()}</code></pre> \n"
    return final_output

@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')

if __name__ == "__main__":
    app.run(port=port)
