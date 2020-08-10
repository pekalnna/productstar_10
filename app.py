from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

with sqlite3.connect('inner.db') as cn:
    crs = cn.cursor()
    crs.execute('DROP TABLE IF EXISTS t;')
    cn.commit()
    crs.execute('CREATE TABLE t(key TEXT PRIMARY KEY, q INT)')
    cn.commit()


@app.route('/api/')
def api_work():
    try:
        key = request.args.get('key')
        q = int(request.args.get('q'))
        with sqlite3.connect('inner.db') as cn:
            crs = cn.cursor()
            crs.execute('''
            INSERT INTO t(key, q) VALUES (:key, :q) 
            ON CONFLICT(key) DO UPDATE
            SET q = q + :q
            WHERE key = :key
            ''', {'key':key, 'q':q})
            cn.commit()
            crs.execute('SELECT key, q FROM t WHERE key = ?', key)
            rs = crs.fetchall()
        if rs:
            return jsonify(key=rs[0][0], q=rs[0][1])
    except Exception as e:
        app.logger.error(e)
        return render_template('hello.html')
