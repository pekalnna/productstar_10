from flask import Flask, url_for
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'''
    <h2> This is The Main page!</h2>
    Some link here
    <a href = {url_for('hello_first')} > first </a>
    <a href = {url_for('hello_second')} > second </a>
    '''


@app.route('/first')
def hello_first():
    return f'''
    <h2> This is First page!</h2>
    <a href = {url_for('hello_world')} > main </a>
    <a href = {url_for('hello_second')} > second </a>
    '''


@app.route('/second')
def hello_second():
    return f'''
    <h2> This is Second page!</h2>
    <a href = {url_for('hello_world')} > main </a>
    <a href = {url_for('hello_first')} > first </a>
    '''
