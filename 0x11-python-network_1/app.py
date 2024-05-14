#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index"

@app.route('/status_401')
def status_401():
    return "Unauthorized", 401

@app.route('/doesnt_exist')
def doesnt_exist():
    return "Not Found", 404

@app.route('/status_500')
def status_500():
    return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
