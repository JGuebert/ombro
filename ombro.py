from flask import Flask, render_template, redirect, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    subprocess.Popen(['./bin/youtube-dl.exe', request.form['download_url'], '-o', './output/%(title)s.%(ext)s'])
    return redirect('/?download_started=1')