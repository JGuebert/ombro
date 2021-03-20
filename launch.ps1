param (
    [switch]$debug
)

$env:FLASK_APP = '.\ombro.py'
If ($debug) { $env:FLASK_DEBUG = '1' }
flask run
