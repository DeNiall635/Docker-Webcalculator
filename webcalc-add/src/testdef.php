<?php
require('functions.inc.php');

function noParams(){
  $ch = curl_init();
  $url = "http://localhost:8080/";
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $data = curl_exec($ch);
  curl_close($ch);

  $expected = '{"error":true,"string":"Missing Parameter(s)","answer":0}';

  if($data == $expected)
  {
      echo "Test noParams Passed\n";
      echo "Got ".$data." expected ".$expected. "\n";
  }
  else
  {

      echo "Test noParams Failed\n";
      echo "Got ".$data." expected ".$expected. "\n";
      exit(1); // exit code not zero - error
  }

}

function normalAdd(){
  $ch = curl_init();
  $url = "http://localhost:8080/?x=5&y=13";
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $data = curl_exec($ch);
  curl_close($ch);

  $expected = '{"error":false,"string":"5+13=18","answer":18}';

  if($data == $expected)
  {
      echo "Test normalAdd Passed\n";
      echo "Got ".$data." expected ".$expected. "\n";
  }
  else
  {

      echo "Test normalAdd Failed\n";
      echo "Got ".$data." expected ".$expected. "\n";
      exit(1); // exit code not zero - error
  }

}


function addZero(){
  $ch = curl_init();
  $url = "http://localhost:8080/?x=5&y=0";
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $data = curl_exec($ch);
  curl_close($ch);

  $expected = '{"error":false,"string":"5+0=5","answer":5}';

  if($data == $expected)
  {
      echo "Test AddZero Passed\n";
      echo "Got ".$data." expected ".$expected. "\n";
  }
  else
  {

      echo "Test AddZero Failed\n";
      echo "Got ".$data." expected ".$expected. "\n";
      exit(1); // exit code not zero - error
  }

}

function addPositiveNegative(){
  $ch = curl_init();
  $url = "http://localhost:8080/?x=5&y=-10";
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $data = curl_exec($ch);
  curl_close($ch);

  $expected = '{"error":false,"string":"5+-10=-5","answer":-5}';

  if($data == $expected)
  {
      echo "Test addPositiveNegative Passed\n";
      echo "Got ".$data." expected ".$expected. "\n";
  }
  else
  {

      echo "Test addPositiveNegative Failed\n";
      echo "Got ".$data." expected ".$expected. "\n";
      exit(1); // exit code not zero - error
  }

}


function addNegativeNegative(){
  $ch = curl_init();
  $url = "http://localhost:8080/?x=-5&y=-10";
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $data = curl_exec($ch);
  curl_close($ch);

  $expected = '{"error":false,"string":"-5+-10=-15","answer":-15}';

  if($data == $expected)
  {
      echo "Test addNegativeNegative Passed\n";
      echo "Got ".$data." expected ".$expected. "\n";
  }
  else
  {

      echo "Test addNegativeNegative Failed\n";
      echo "Got ".$data." expected ".$expected. "\n";
      exit(1); // exit code not zero - error
  }

}


function addNegativePositive(){
  $ch = curl_init();
  $url = "http://localhost:8080/?x=-5&y=10";
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $data = curl_exec($ch);
  curl_close($ch);

  $expected = '{"error":false,"string":"-5+10=5","answer":5}';

  if($data == $expected)
  {
      echo "Test addNegativePositive Passed\n";
      echo "Got ".$data." expected ".$expected. "\n";
  }
  else
  {

      echo "Test addNegativePositive Failed\n";
      echo "Got ".$data." expected ".$expected. "\n";
      exit(1); // exit code not zero - error
  }

}


function singleMissingParam(){
  $ch = curl_init();
  $url = "http://localhost:8080/?x=-5";
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $data = curl_exec($ch);
  curl_close($ch);

  $expected = '{"error":true,"string":"Missing Parameter(s)","answer":0}';

  if($data == $expected)
  {
      echo "Test singleMissingParam Passed\n";
      echo "Got ".$data." expected ".$expected. "\n";
  }
  else
  {

      echo "Test singleMissingParam Failed\n";
      echo "Got ".$data." expected ".$expected. "\n";
      exit(1); // exit code not zero - error
  }

}


function nonIntParam(){
  $ch = curl_init();
  $url = "http://localhost:8080/?x=-5&y=apple";
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $data = curl_exec($ch);
  curl_close($ch);

  $expected = '{"error":true,"string":"Non int value","answer":0}';

  if($data == $expected)
  {
      echo "Test nonIntParam Passed\n";
      echo "Got ".$data." expected ".$expected. "\n";
  }
  else
  {

      echo "Test nonIntParam Failed\n";
      echo "Got ".$data." expected ".$expected. "\n";
      exit(1); // exit code not zero - error
  }
}


function addFunctionTest(){

  $x=10;
  $y=5;
  $expect=15;

  $answer=add($x,$y);

  echo "Test Result: ".$x."+".$y."=".$answer." (expected: ".$expect.")\n";

  if ($answer==$expect)
  {
      echo "Test addFunctionTest Passed\n";
       // exit code 0 - success
  }
  else
  {
      echo "Test Failed\n";
      exit(1); // exit code not zero - error
  }

}
