<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('functions.inc.php');

$output = array(
	"error" => false,
	"string" => "",
	"answer" => 0
);

$x = $_REQUEST['x'];
$y = $_REQUEST['y'];
if($x === NULL || $y === NULL){
	$output['error'] = true;
	$output['string'] = 'Missing Parameter(s)';
}else{

	$x_int = intval($x);
	$y_int = intval($y); //not int values come out as zeros



	//after converting to int non ints will be zero
	//php 3 == '3' is true
	// so after chaging to int can check if param was int or not
	//converting to strings as 0 == "apple" is true as apple is converted to int as 0
	if(strval($x) != strval($x_int) || strval($y) != strval($y_int)){
		$output['error'] = true;
		$output['string']='Non int value';
	}else{
		$answer=add($x_int,$y_int);
		$output['string']=$x_int."+".$y_int."=".$answer;
		$output['answer']=$answer;

	}

}


echo json_encode($output);
exit();
