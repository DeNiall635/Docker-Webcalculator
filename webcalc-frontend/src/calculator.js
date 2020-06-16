
let value = 0;
let x = 0;
let y = 0;
let operation = '';



let operationMap = externalOperationMap;

let ProxyURL = "http://proxy.40173800.qpc.hal.davecutting.uk"

function Display()
{
    document.getElementById('display').value = value;
}

function Clear()
{
    value = 0;
    x = 0;
    y = 0;
    operation = '';
    Display();
}

function NumClick(n)
{
    if (value == 0)
        value = n;
    else
    {
        value *= 10;
        value += n;
    }

    Display();
}


function MathOperation(op)
{
    // if we have an outstanding operation resolve it
    if (operation != '')
      Equals();

    x = value;
    value = 0;
    operation = op;

    Display();
}

function Equals()
{
    if (operation == '')
        return;

    y = value;


    if(operationMap[operation] == undefined){
      // incorrect operation (shouldnt really be possible)
      value = "Unknown operation";
      Display();
      //display Error but have the value be 0 for future functions
      value = 0;
    }else{
      //correct MathOperation
      //let ans = x+y; // nah - too easy :)

      let xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
              var j = JSON.parse(this.response);
              console.log(j)
              x=0;
              y=0;
              operation='';

              if(j.error){
                value = j.string;
                Display();
                //display Error but have the value be 0 for future functions
                value = 0;
              }else{
                value = j.answer;
                Display();
              }



              //would do error handling in here as well
              // if the json comes back with true in error value would need to display this appropiatly
          }
      };
      //Cacl display will show "Calculating while waiting on response back"
      value = "Calculating..."
      Display();

      xhttp.open("GET",ProxyURL + "?operation="+operationMap[operation]+"&x="+x+"&y="+y);
      //xhttp.open("GET", dict[operation] +"?x="+x+"&y="+y)
      //xhttp.open("GET", "http://127.0.0.1:5000/" + "?operation="+operationMap[operation]+"&x="+x+"&y="+y)
      xhttp.send();
      return;
    }
}
