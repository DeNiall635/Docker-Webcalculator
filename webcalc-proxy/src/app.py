from flask import Flask, request, redirect, make_response
import json
import requests
app = Flask(__name__)

@app.route('/')
def hello_proxy():
    operation = request.args.get("operation")

    f = open("functions.json", "r")

    #creats a dict from the json file
    functions_dict = json.load(f)

    f.close()
    functions_dict = functions_dict["functions"]


    valid_operation = functions_dict.get(str(operation))

    #check url and dict
    if(operation == None or valid_operation == None):
        output = {
        "error": True,
        "string": "Missing or Incorrect Parameters",
        "answer": 0
        }
        json_result = json.dumps(output)
        resp = make_response(json_result)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Content-Type'] = 'application/json'
        return resp
    else:
        parameter_string = "?x="+ str(request.args.get("x")) +"&y=" + str(request.args.get("y"))
        full_url = valid_operation + parameter_string

        json_response = requests.get(full_url)

        if(json_response.status_code == 200):
            resp = make_response(json_response.text)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Content-Type'] = 'application/json'
            #think need to return json rather than redirect
            return resp
        else:
            output = {
            "error": True,
            "string": "Not a Valid Response",
            "answer": 0
            }
            json_result = json.dumps(output)
            resp = make_response(json_result)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Content-Type'] = 'application/json'
            return resp

@app.route('/info')
def info():

    f = open("functions.json", "r")
    functions_dict = json.load(f)
    f.close()
    functions_dict = functions_dict["functions"]

    html_output = "<h1>Available functions and Urls</h1>"

    html_output = html_output + "<h2>There are " + str(len(functions_dict)) + " functions available: </h2>"



    for key in functions_dict:

        html_string = "<p> Function: <b>" + str(key) + "</b> has url: <a href=" +str(functions_dict[key]) + ">" + str(functions_dict[key]) + "</a></p><hr>"
        html_output = html_output + html_string

    return html_output


@app.route('/functions')
def functions():

    f = open("functions.json", "r")

    #creats a dict from the json file
    functions_dict = json.load(f)

    f.close()

    json_from_dict = json.dumps(functions_dict)

    resp = make_response(json_from_dict)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'


    return resp

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
    #app.run(debug = True)
