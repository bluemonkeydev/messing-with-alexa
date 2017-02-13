from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

@app.route('/')
def homepage():
    return 'In Sioux Falls there is a wind chill warning in effect until noon on Sunday. The current weather is -29 degrees with intermittent clouds. Wait, what the fuck? Are you serious? Is is -29 degrees? Where the hell is Sioux Falls? Screw this, put me back in the box and send me to Florida. You are fucking insane.'

@ask.launch
def start_skill():
    welcome_message = 'Snow is very likely in Sioux Falls tonight. There is a 97 percent chance. By the way, Phil Shrek said it was going to snow like mother fucker until tomorrow at noon.'
    print welcome_message
    return statement(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    yes_text = 'Hi, I love you'
    print yes_text
    return statement(yes_text)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Ok, sorry to bother you. I will be quiet now'
    print bye_text
    return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=True)