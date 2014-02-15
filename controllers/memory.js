var os = require('os');

exports.getActual = function(){
	    	var actualValue = {
			freemem: os.freemem(),
			totalmem: os.totalmem(),
			load: os.freemem() / os.totalmem()
		};
		return actualValue;		
    }
