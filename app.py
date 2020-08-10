from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/first')
def hello_first():
    return 'Hello, First!'


@app.route('/second')
def hello_second():
    return 'Hello, Next!'
