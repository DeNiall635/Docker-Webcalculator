package main

import (
    "testing"
    function "./function"
    //"net/http"
    //"log"
    //"net/http/httptest"
    //"io"
    //"io/ioutil"
)

func TestMultiply(t *testing.T){
  answer := function.Multiply(4, 5)
  //multiply := 2 * 3
  if answer != 20 {
    t.Error("Expected 20 got ", answer)
  }
}
