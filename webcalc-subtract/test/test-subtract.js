var expect  = require('chai').expect;
var sub = require('../subtract');

//Add Testing For Web Server Changes
it('Response OK (200)', function(done){
  request('http://0.0.0.0:80', function(error, response, body){
    expect(response.statusCode).to.equal(200);
    done();
  });
});

it('Web No parameters', function(done){
  request('http://0.0.0.0:80', function(error, response, body){
    expect(body).to.equal('{"error":true,"string":"Parameter(s) missing","answer":0}');
    done();
  });
});

it('Web Normal subtraction', function(done){
  request('http://0.0.0.0:80/?x=10&y=8', function(error, response, body){
    expect(body).to.equal('{"error":false,"string":"10-8=2","answer":2}');
    done();
  });
});

it('Web Subtract gives negative answer', function(done){
  request('http://0.0.0.0:80/?x=2&y=8', function(error, response, body){
    expect(body).to.equal('{"error":false,"string":"2-8=-6","answer":-6}');
    done();
  });
});

it('Web Subtract negative number', function(done){
  request('http://0.0.0.0:80/?x=2&y=-8', function(error, response, body){
    expect(body).to.equal('{"error":false,"string":"2--8=10","answer":10}');
    done();
  });
});

it('Web Subtract zero', function(done){
  request('http://0.0.0.0:80/?x=2&y=0', function(error, response, body){
    expect(body).to.equal('{"error":false,"string":"2-0=2","answer":2}');
    done();
  });
});


it('Web Subtract missing one param', function(done){
  request('http://0.0.0.0:80/?x=2', function(error, response, body){
    expect(body).to.equal('{"error":true,"string":"Parameter(s) missing","answer":0}');
    done();
  });
});

it('Web Parameter isnt number', function(done){
  request('http://0.0.0.0:80/?x=10&y=hello', function(error, response, body){
    expect(body).to.equal('{"error":true,"string":"Non int value","answer":0}');
    done();
  });
});


//----------------------------------------------------------------------------------------
//#######################################################################################
//----------------------------------------------------------------------------------------

//test live url
it('LIVE Response OK (200)', function(done){
  request('http://subtract.40173800.qpc.hal.davecutting.uk/', function(error, response, body){
    expect(response.statusCode).to.equal(200);
    done();
  });
});


it('LIVE Web No parameters', function(done){
  request('http://subtract.40173800.qpc.hal.davecutting.uk/', function(error, response, body){
    expect(body).to.equal('{"error":true,"string":"","answer":0}');
    done();
  });
});

it('LIVE Web Normal subtraction', function(done){
  request('http://subtract.40173800.qpc.hal.davecutting.uk/?x=10&y=8', function(error, response, body){
    expect(body).to.equal('{"error":false,"string":"10-8=2","answer":2}');
    done();
  });
});

it('LIVE Web Subtract gives negative answer', function(done){
  request('http://subtract.40173800.qpc.hal.davecutting.uk/?x=2&y=8', function(error, response, body){
    expect(body).to.equal('{"error":false,"string":"2-8=-6","answer":-6}');
    done();
  });
});

it('LIVE Web Subtract negative number', function(done){
  request('http://subtract.40173800.qpc.hal.davecutting.uk/?x=2&y=-8', function(error, response, body){
    expect(body).to.equal('{"error":false,"string":"2--8=10","answer":10}');
    done();
  });
});

it('LIVE Web Subtract zero', function(done){
  request('http://subtract.40173800.qpc.hal.davecutting.uk/?x=2&y=0', function(error, response, body){
    expect(body).to.equal('{"error":false,"string":"2-0=2","answer":2}');
    done();
  });
});


it('LIVE Web Subtract missing one param', function(done){
  request('http://subtract.40173800.qpc.hal.davecutting.uk/?x=2', function(error, response, body){
    expect(body).to.equal('{"error":true,"string":"","answer":0}');
    done();
  });
});

it('LIVE Web Parameter isnt number', function(done){
  request('http://subtract.40173800.qpc.hal.davecutting.uk/?x=10&y=hello', function(error, response, body){
    expect(body).to.equal('{"error":true,"string":"","answer":0}');
    done();
  });
});




//Original Test for Subtraction
it('Subtraction Test', function(done) {
        var x = 10;
        var y = 5;
        var a = x-y;
        expect(sub.subtract(x,y)).to.equal(a);
        done();
});
