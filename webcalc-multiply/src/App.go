package main

import (
    //"fmt"
    "net/http"
    "log"
    "strconv"
    function "./function"
    "encoding/json"
)

type Response struct {
  Error bool  `json:"error"`
  String string `json:"string"`
  Answer int `json:"answer"`
}


func main() {
    http.HandleFunc("/", HelloServer)
    http.ListenAndServe(":8080", nil)
}

func HelloServer(w http.ResponseWriter, r *http.Request) {
    //"dictionary" keys have to be capatilised in order to export them
    // fun feature of golang!!!
    //so will likly have to change json keys everywhere for consistency
    output := Response{
      Error: false  ,
      String: "",
      Answer: 0,
    }

    query := r.URL.Query()
    x := query.Get("x")
    y := query.Get("y")

    if len(x) < 1 || len(y) < 1{
      log.Println("A parameter doesn't exist")
      output.Error = true
      output.String = "Missing parameter(s)"
    }else{
      x_int, x_error := strconv.Atoi(x)
      y_int, y_error := strconv.Atoi(y)

      if x_error != nil || y_error != nil{
        // if unable to convert to int
        log.Println("Unable to convert x or y to int")
        output.Error = true
        output.String = "Non int value"
      }else{
        answer := function.Multiply(x_int, y_int)
        output.Answer = answer
        output.Error = false
        output.String = x + "*" + y + "=" + strconv.Itoa(answer)
        log.Println("Successful answer")
      }
    }

    //fmt.Fprintf(w, "Error: " + strconv.FormatBool(output.Error) + "\n")
    //fmt.Fprintf(w, "Answer string: " + strconv.Itoa(output.Answer)+ "\n")
    //fmt.Fprintf(w, "Answer: " + output.String + "\n")

    //thing, _ := json.Marshal(output)
    //log.Println(string(thing))

    //fmt.Fprintf(w, string(thing))

    w.Header().Set("Access-Control-Allow-Origin", "*")
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(output)

}
