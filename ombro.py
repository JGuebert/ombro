from flask import Flask, render_template, redirect, request
import subprocess
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    context = {}
    context['download_name'] = request.args.get('download_started', type=str)
    return render_template('index.html', context=context)

@app.route('/download', methods=['POST'])
def download():
    download_name = subprocess.run(['./bin/youtube-dl.exe', request.form['download_url'], '-e'], capture_output=True).stdout
    download = subprocess.Popen(['./bin/youtube-dl.exe', request.form['download_url'], '-o', './output/%(title)s.%(ext)s'])
    redirect_path = '/?download_started=' + str(urllib.parse.quote(download_name))
    return redirect(redirect_path)