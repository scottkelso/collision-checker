// dependencies
var restify = require('restify');
var builder = require('botbuilder');
var request = require('request');
// var natural = require('natural');

// Setup Restify Server
var server = restify.createServer();
server.listen(process.env.port || process.env.PORT || 3978, function () {
   console.log('%s listening to %s', server.name, server.url); 
});


// Create chat connector for communicating with the Bot Framework Service
var connector = new builder.ChatConnector({
    appId: process.env.MICROSOFT_APP_ID,
    appPassword: process.env.MICROSOFT_APP_PASSWORD
});

// create the bot
var bot = new builder.UniversalBot(connector);

// Listen for messages from users 
server.post('/collisionBot', connector.listen());

//entry point for branches and receving an image
var bot = new builder.UniversalBot(connector, function(session){
	var msg = "Hi there, I am the collision checker chatbot. I'm hear to answer some questions. Ask me what I can do or for some help and I will tell you what I can do!"
	session.send(msg);
});

// TEST DIALOGUES
bot.dialog('Test', [
	function (session) {
		getTestData('', function(response) {
			session.endDialog(response)
		})
    }
]).triggerAction({
    matches: /hello world/i
});

bot.dialog('TestPost', [
	function (session) {
		postData('Test', function(response) {
			session.endDialog(response)
		})
    }
]).triggerAction({
    matches: /post/i
});

var locations = {

}
var locations = {
    "Northern Ireland": {
        value: 0
    },
    "Belfast City": {
        value: 7
    },
    "Lisburn": {
        value: 24
    },
    "Newtownards": {
        value: 14
    }
}

// ACTUAL DIALOGS HERE
bot.dialog('ChanceOfFatalitiesCollisions', [
	function(session) {
		var msg = "Where would you like to hear about? You can choose the entire of Northern Ireland or a specific area.\n1. Northern Ireland \n2. Belfast \n3. Lisburn \n4. Newtownards"
		builder.Prompts.text(session, msg)
	},
	function (session, result) {
		var choice = result.response
		switch(choice) {
			case "Northern Ireland":
				getFatalCollisions(session)
				break;
			case "Belfast":
				getFatalCollisionsForArea(session, {value:7, name:"Belfast"})
				break;
			case "Lisburn":
				getFatalCollisionsForArea(session, {value:24, name:"Lisburn"})
				break;
			case "Newtownards":
				getFatalCollisionsForArea(session, {value:14, name:"Newtownards"})
				break;
		}		
    }
]).triggerAction({
    matches: /fatalities|fatality|fatal/i
});

function getFatalCollisions(session) {
	request('http://localhost:5000/chanceOfFatalitiesCollisions', function (error, response, body) {
		var msg = "There have been " + body + " fatal collisions recorded in Northern Ireland in the past 2 years."
		session.endDialog(msg);
	});
}

function getFatalCollisionsForArea(session, area) {
	request.post('http://localhost:5000/chanceOfFatalitiesCollisionsInArea', 
	{form:{key:area.value}}, 
	function(error, response, body){
		var msg = "There have been " + body + " fatal collisions recorded in " + area.name + " in the past 2 years."
		session.endDialog(msg);
	});
}

bot.dialog('ChanceOfSeriousCollisions', [
	function(session) {
		var msg = "Where would you like to hear about? You can choose the entire of Northern Ireland or a specific area.\n1. Northern Ireland \n2. Belfast \n3. Lisburn \n4. Newtownards"
		builder.Prompts.text(session, msg)
	},
	function (session, result) {
		var choice = result.response
		switch(choice) {
			case "Northern Ireland":
				getSeriousCollisions(session)
				break;
			case "Belfast":
				getSeriousCollisionsForArea(session, {value:7, name:"Belfast"})
				break;
			case "Lisburn":
				getSeriousCollisionsForArea(session, {value:24, name:"Lisburn"})
				break;
			case "Newtownards":
				getSeriousCollisionsForArea(session, {value:14, name:"Newtownards"})
				break;
		}		
    }
]).triggerAction({
    matches: /serious/i
});

function getSeriousCollisions(session) {
	request('http://localhost:5000/chanceOfSeriousCollisions', function (error, response, body) {
		var msg = "There have been " + body + " serious collisions recorded in Northern Ireland in the past 2 years."
		session.endDialog(msg);
	});
}

function getSeriousCollisionsForArea(session, area) {
	request.post('http://localhost:5000/chanceOfSeriousCollisionsInArea', 
	{form:{key:area.value}}, 
	function(error, response, body){
		var msg = "There have been " + body + " serious collisions recorded in " + area.name + " in the past 2 years."
		session.endDialog(msg);
	});
}

bot.dialog('ChanceOfSlightInjuryCollisions', [
	function(session) {
		var msg = "Where would you like to hear about? You can choose the entire of Northern Ireland or a specific area.\n1. Northern Ireland \n2. Belfast \n3. Lisburn \n4. Newtownards"
		builder.Prompts.text(session, msg)
	},
	function (session, result) {
		var choice = result.response
		switch(choice) {
			case "Northern Ireland":
				getMinorCollisions(session)
				break;
			case "Belfast":
				getMinorCollisionsForArea(session, {value:7, name:"Belfast"})
				break;
			case "Lisburn":
				getMinorCollisionsForArea(session, {value:24, name:"Lisburn"})
				break;
			case "Newtownards":
				getMinorCollisionsForArea(session, {value:14, name:"Newtownards"})
				break;
		}		
    }
]).triggerAction({
    matches: /slight|minor/i
});

function getMinorCollisions(session) {
	request('http://localhost:5000/chanceOfSlightInjuryCollisions', function (error, response, body) {
		var msg = "There have been " + body + " minor collisions recorded in Northern Ireland in the past 2 years."
		session.endDialog(msg);
	});
}

function getMinorCollisionsForArea(session, area) {
	request.post('http://localhost:5000/chanceOfSlightInjuryCollisionsInArea', 
	{form:{key:area.value}}, 
	function(error, response, body){
		var msg = "There have been " + body + " minor collisions recorded in " + area.name + " in the past 2 years."
		session.endDialog(msg);
	});
}



//get request example
//usage
//    	 getData('', function (msg) {
//            console.log(msg)
//         });
function getTestData(data, success){
	request('http://localhost:5000/placeholder_get', function (error, response, body) {
		success(body);
	});
}

//post request example
//you can also post images! if sending image form a chatbot use 'fs' module to load the image url and then send it.
//usage
   	//  postData('data', function (msg) {
    //         console.log(msg)
    //     });

function postData(data, cb){
	request.post('http://localhost:5000/chanceOfFatalitiesCollisionsInArea', {form:{key:data}}, function(error, response, body){
  	   	cb(body)
	});
}