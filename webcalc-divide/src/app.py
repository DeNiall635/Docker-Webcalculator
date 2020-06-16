from flask import Flask
from flask import request
from flask import Response
from divide import divide
import json
import flask

app = Flask(__name__)

@app.route('/')
def web_request():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))

    result = divide(int(x),int(y))

    output = {
        "error": False,
        "string": "%s%s%s=%s" % (x, "/", y, result),
        "answer": result
    };


    json_array = json.dumps(output)
    rep = flask.Response(json_array)
    rep.headers['Content-Type'] = "application/json"
    rep.headers['Access-Control-Allow-Origin'] = "*"

    return rep


@app.errorhandler(500)
def internal_error(error):
    output500 = {
    "error": True,
    "string": "Missing Parameters",
    "answer": 0
    };

    json_array = json.dumps(output500)
    rep500 = flask.Response(json_array)
    rep500.headers['Content-Type'] = "application/json"
    rep500.headers['Access-Control-Allow-Origin'] = "*"

    return rep500

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
