<?php
echo "Test Script Starting\n";
//require('functions.inc.php');
require('testdef.php');

noParams();
normalAdd();
addZero();
addPositiveNegative();
addNegativeNegative();
singleMissingParam();
nonIntParam();
addFunctionTest();


//if we make it to the end we have pass all tests so
exit(0); // success

//if any of above tests fail they will exit with code 1 - i.e. fail
