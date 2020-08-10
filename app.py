from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/api/')
def api_work():
    try:
        n = int(request.args.get('n'))
        if n > 0:
            return jsonify(m=n + 1, some_data=''.join([str(n) for x in range(n)]))
    except:
        return render_template('hello.html')
