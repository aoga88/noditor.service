var mongoose = require('mongoose');
var memorySchema = mongoose.Schema({
	server: {
		name: String,
		ip: String,
		os: String
	},
	date: {type: Date, default: Date.now},
	freemem: Number,
	totalmem: Number,
	load: Number
}, {collection: 'memory'});

exports.memory = mongoose.model('memory', memorySchema);