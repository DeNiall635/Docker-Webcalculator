'use strict';

const express = require('express');

const PORT = 80;
const HOST = '0.0.0.0';

var sub = require('./subtract');

const app = express();
app.get('/', (req,res) => {

    var output = {
        'error': false,
        'string': '',
        'answer': 0
    };

    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*')
    var x = req.query.x;
    var y = req.query.y;

//Add Error Handiling for undefiend Variables
    if(x === undefined || y === undefined){
      output.error = true;
      output.string = "Parameter(s) missing";
    }else{
      var x_int = parseInt(x)
      var y_int = parseInt(y)

      if(isNaN(x_int) || isNaN(y_int)){
        // non number
        output.error = true;
        output.string = "Non int value";
      }else{

    var answer = sub.subtract(x_int,y_int);

    output.string = x + '-' + y + '=' + answer;
    output.answer = answer;
	}
}

    res.end(JSON.stringify(output));
});

app.listen(PORT, HOST);
