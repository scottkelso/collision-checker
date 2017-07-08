from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/placeholder_get', methods=['GET'])
def placeholder_get():
    return "Hello, World!"

@app.route('/chanceOfFatalitiesCollisions', methods=['GET'])
def get_fatalities_collision_count():
    return str(210)

@app.route('/chanceOfSeriousCollisions', methods=['GET'])
def get_serious_collision_count():
    return str(2141)

@app.route('/chanceOfSlightInjuryCollisions', methods=['GET'])
def get_slight_injury_collision_count():
    return str(25961)

@app.route('/chanceOfFatalitiesCollisionsInArea', methods=['POST'])
def get_fatalities_collision_count_for_area():
    print(request.form['key'])
    return str(10)

@app.route('/chanceOfSeriousCollisionsInArea', methods=['POST'])
def get_serious_collision_count_for_area():
    print(request.form['key'])
    return str(12)

@app.route('/chanceOfSlightInjuryCollisionsInArea', methods=['POST'])
def get_slight_injury_collision_count_for_area():
    print(request.form['key'])
    return str(19)

if __name__ == '__main__':
    app.run(debug=True)