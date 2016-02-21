import io
from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('home.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)