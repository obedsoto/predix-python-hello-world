import flask
import os

app = flask.Flask(__name__)

port = int(os.getenv("PORT", 0))


@app.route('/')
def hello_world():
    return "Hello World from python"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
