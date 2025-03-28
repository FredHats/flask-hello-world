from flask import Flask, render_template
app = Flask(__name__)
app.run(host='0.0.0.0', port=5000)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/message')
def message():
    return "ciao sono Fritz"
