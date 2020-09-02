from flask import Flask, render_template
app = Flask(__name__)

@app.route('/a/<path:path>')
def a(path):
    return render_template('a.html', path=path)


@app.route('/b')
def b():
    return render_template('b.html')
