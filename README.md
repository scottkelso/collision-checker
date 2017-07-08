# Chatbot Collision Checker
This is a chatbot that can help predict collisions in Northern Ireland!

## Technology Stack
* Python
* Javascript
* Nodejs

## How it works
There is a machine learning algorithm written in python which uses historical traffic collision data from the past 3 years to make predictions based on...

* weather conditions
* time of the day
* day of the week
* and location.

This is fronted by a chatbot which can answer questions that its user has about the data. Questions such as...

* What time in the day do most collisions occur?
* Show me a map of collisions in Northern Ireland
* What is the probability of a collision in Antrim today?

## Development
*NOTE* A bot emulator is required to test the chatbot. We use the following application:
botframework-emulator-3.5.29-x86_64.AppImage

The chatbot node server requires *nodemon* to be installed. Use the following command to install it inside the chatbot directory.

`sudo npm install -g nodemon`

And then to run it...

`nodemon index.js`

Now your bot emulator should be able to connect to the server.

To run the python server run the following command in the backend directory...

`python app.py`

Now this allows the nodejs server to hit endpoints that relate to requesting data from the machine learning algorithm.

## Colaberators

-Jake 
-Josh


