from flask import Flask, request, redirect, make_response
import json
import requests
from random import randrange
import datetime
import time
app = Flask(__name__)

#here is am defining what the expected results output would be for each of the functions in order to test them hrere
#the result from these will give what should be expected from each of the http functions
def addition(x, y):
    return x+y

def subtraction(x, y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if(y == 0):
        return 0
    else:
        return int(x/y)

def modulo(x,y):
    if(y == 0):
        return 0
    else:
        return x%y

def square(x,y):
    return pow(x,2)

#creating a dictionary to act as a switch startment for when we need to call each function when testing
dict_functions = {
    "add": addition,
    "sub": subtraction,
    "mul": multiplication,
    "div": division,
    "mod": modulo,
    "sqr": square
}
#end of expected functions


#Home route which displays links to the testing and results pages
@app.route('/')
def hello_world():
    html_output = "<h1>Whats here?</h1> <br/>"

    html_output = html_output + " <h2>1.)</h2><h3>HTTP request Tests</h3> <p><a href=/test> Testing link </a></p><hr>"

    html_output = html_output + " <h2>2.)</h2><h3>View results</h3> <p><a href=/results> Results link </a></p><hr>"
    return html_output



@app.route('/test')
def test_service():

    #the proxy service has an enpoint which returns json result with all functions it has and thier urls
    #so I use that to get the list of functions and their urls
    #in the dictionary the key is the function name i.e. "add" and the value is its url
    full_url = "http://proxy.40173800.qpc.hal.davecutting.uk/functions"
    json_response = requests.get(full_url)

    functions_dict = json.loads(json_response.text)
    functions_dict = functions_dict["functions"]

    #construction the output html
    output_html = ""

    for key in functions_dict:

        output_html = output_html + "<h3>Tests for function " + str(key) + "</h3>"

        #range 1-6 so do 5 tests for each function
        for i in range(1, 6):

            #randome numbers for testing
            rand_x = randrange(10)
            rand_y = randrange(10)

            #creating the url to get the result
            function_url = str(functions_dict[key])+ "?x=" + str(rand_x) + "&y=" + str(rand_y)


            #timing and getting the result here
            start_time = time.time()
            result_json_response = requests.get(function_url)
            end_time = time.time()
            total_time = end_time - start_time
            #timinng end

            #convert json result to dictionary to easily extract values
            result_dictionary = json.loads(result_json_response.text)
            answer = result_dictionary.get("answer")
            calculation = result_dictionary.get("string")
            calculation = str(rand_x) + str(key) + str(rand_y)
            expected = dict_functions[key](rand_x, rand_y)
            is_correct = answer == expected # may need to do string conversion or something


            #have results now construct output_html
            correct_string = "Correct" if is_correct else "incorrect"
            current_time = "[" + str(datetime.datetime.now().time()) + "]"
            output_string = current_time + " For " + str(calculation) + " the expected answer was " + str(expected) + " and the answer recieved was " + str(answer) + ". The response was " + correct_string + " and took " + str(total_time) + " seconds"
            output_line_html = "<p>"+ output_string + "</p>"
            output_html = output_html + output_line_html

            #write the result to a text file as a kind of primative storage
            f = open("data_storage.txt", "a")
            f.write(output_string + "\n")
            f.close()



    #for each function , for 1-10 : get random numbers do request, get time, result, compare result to expected


    return output_html


@app.route('/results')
def results():
    #opening the storage file and reading all of the lines within it
    f = open("data_storage.txt", "r")
    all_lines = f.readlines()
    f.close()

    output_html = "<h1>All results </h1>"

    #outputing each line from the storage file into a paragraph and displaying it
    for line in all_lines:
        output = "<p>" + line + "</p> <hr>"
        output_html = output_html + output

    return output_html

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
    #app.run(debug = True)
