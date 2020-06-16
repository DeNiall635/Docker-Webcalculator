package main

import (


    "net/http/httptest"
    "io/ioutil"
    "testing"
    "strings"
)



func TestNoParams(t *testing.T){

  handler := HelloServer
  req := httptest.NewRequest("GET", "http://localhost:8083/", nil)
  w := httptest.NewRecorder()
  handler(w, req)

  resp := w.Result()
  body, _ := ioutil.ReadAll(resp.Body)


  json_response := strings.TrimRight(string(body), "\n")

  expected := `{"error":true,"string":"Missing parameter(s)","answer":0}`

  if json_response != expected {
    t.Error(expected + " got: ", json_response)
  }
}


func TestNormalMultiply(t *testing.T){

  handler := HelloServer
  req := httptest.NewRequest("GET", "http://localhost:8083/?x=5&y=3", nil)
  w := httptest.NewRecorder()
  handler(w, req)

  resp := w.Result()
  body, _ := ioutil.ReadAll(resp.Body)


  json_response := strings.TrimRight(string(body), "\n")

  expected := `{"error":false,"string":"5*3=15","answer":15}`

  if json_response != expected {
    t.Error(expected + " got: ", json_response)
  }
}


func TestMultiplyZero(t *testing.T){

  handler := HelloServer
  req := httptest.NewRequest("GET", "http://localhost:8083/?x=5&y=0", nil)
  w := httptest.NewRecorder()
  handler(w, req)

  resp := w.Result()
  body, _ := ioutil.ReadAll(resp.Body)


  json_response := strings.TrimRight(string(body), "\n")

  expected := `{"error":false,"string":"5*0=0","answer":0}`

  if json_response != expected {
    t.Error(expected + " got: ", json_response)
  }
}


func TestMultiplyNegative(t *testing.T){

  handler := HelloServer
  req := httptest.NewRequest("GET", "http://localhost:8083/?x=5&y=-3", nil)
  w := httptest.NewRecorder()
  handler(w, req)

  resp := w.Result()
  body, _ := ioutil.ReadAll(resp.Body)


  json_response := strings.TrimRight(string(body), "\n")

  expected := `{"error":false,"string":"5*-3=-15","answer":-15}`

  if json_response != expected {
    t.Error(expected + " got: ", json_response)
  }
}


func TestMultiplyMissingSingleParam(t *testing.T){

  handler := HelloServer
  req := httptest.NewRequest("GET", "http://localhost:8083/?x=5", nil)
  w := httptest.NewRecorder()
  handler(w, req)

  resp := w.Result()
  body, _ := ioutil.ReadAll(resp.Body)


  json_response := strings.TrimRight(string(body), "\n")

  expected := `{"error":true,"string":"Missing parameter(s)","answer":0}`

  if json_response != expected {
    t.Error(expected + " got: ", json_response)
  }
}


func TestMultiplyNonIntParam(t *testing.T){

  handler := HelloServer
  req := httptest.NewRequest("GET", "http://localhost:8083/?x=3&y=green", nil)
  w := httptest.NewRecorder()
  handler(w, req)

  resp := w.Result()
  body, _ := ioutil.ReadAll(resp.Body)

  json_response := strings.TrimRight(string(body), "\n")

  expected := `{"error":true,"string":"Non int value","answer":0}`

  if json_response != expected {
    t.Error(expected + " got: ", json_response)
  }
}
