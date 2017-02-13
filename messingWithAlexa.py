from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

@app.route('/')
def homepage():
    return 'Is it cold outside?'

@ask.launch
def start_skill():
    welcome_message = 'In Sioux Falls there is a wind chill warning in effect until noon on Sunday. The current weather is -29 degrees with intermittent clouds. Wait, what the fuck? Are you serious? Is is -29 degrees? Where the hell is Sioux Falls? Screw this, put me back in the box and send me to Florida. You are fucking insane.'
    print welcome_message
    return statement(welcome_message)


if __name__ == '__main__':
    app.run(debug=True)