import flask
import os

app = flask.Flask(__name__)

# get the port from the environment, otherwise get a random number
port = int(os.getenv("PORT", 0))


@app.route('/')
def hello_world():
    body = "Hello World from python<BR /><BR />"
    for x, y in os.environ.items():
        body += x + ": " + y + "<BR />"

    return body


if __name__ == '__main__':
    # 0.0.0.0 externally visible server
    app.run(host='0.0.0.0', port=port)
