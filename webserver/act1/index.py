from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world from web server on py'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')