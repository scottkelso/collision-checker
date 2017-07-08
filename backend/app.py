from flask import Flask
from flask import request
import model as ml

app = Flask(__name__)

@app.route('/placeholder_get', methods=['GET'])
def placeholder_get():
    return "Hello, World!"

@app.route('/collisionCount', methods=['GET'])
def get_collision_count():
    return str(ml.num_of_casualties())

@app.route('/chanceOfFatalitiesCollisions', methods=['GET'])
def get_fatalities_collision_count():
    return str(ml.num_of_fatalities())

@app.route('/chanceOfSeriousCollisions', methods=['GET'])
def get_serious_collision_count():
    return str(ml.num_of_serious())

@app.route('/chanceOfSlightInjuryCollisions', methods=['GET'])
def get_slight_injury_collision_count():
    return str(ml.num_of_slight())

@app.route('/chanceOfFatalitiesCollisionsInArea', methods=['POST'])
def get_fatalities_collision_count_for_area():
    print(request.form['key'])
    return str(46)

@app.route('/chanceOfSeriousCollisionsInArea', methods=['POST'])
def get_serious_collision_count_for_area():
    print(request.form['key'])
    return str(204)

@app.route('/chanceOfSlightInjuryCollisionsInArea', methods=['POST'])
def get_slight_injury_collision_count_for_area():
    print(request.form['key'])
    return str(4190)

@app.route('/collisionProbablility', methods=['GET'])
def get_chance_count():
    prob = ml.predict_ni()
    return "There is a " + "{0:.2f}".format(prob[0]) + "% chance of having a fatal collision and a " + "{0:.2f}".format(prob[1]) + "% chance of a serious collision on average in Northern Ireland."

if __name__ == '__main__':
    app.run(debug=True)