# Ombro
A web-based youtube-dl interface for managing downloads

## Getting Started/Setup
1. Create a Python virtual environment (python -m venv env) and activate it
2. Install the requirements (pip install -r requirements.txt)
3. Put a copy of youtube-dl.exe in a directory named `bin`

*Future updates to Ombro will download youtube-dl automatically if not present and not require a manually supplied version*

## Launching Ombro
If using PowerShell, the included launch.ps1 script will set the FLASK_APP environment variable and start the server.

Otherwise, set the environment variable manually (`export FLASK_APP=ombro.py` or `set FLASK_APP=ombro.py` (Windows Command Prompt)) and then run `flask run`

## Using Ombro
When the server is running, a page will be available at http://localhost:5000 that supports a URL to be passed into youtube-dl.

After clicking submit, the video will be downloaded into a directory named `output`.
