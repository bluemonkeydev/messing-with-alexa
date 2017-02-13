from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

#welcome_message = "dude"
welcome_message = '<speak><s>Team Andy is the group that follows the iconic <break strength="medium"/>Andy\'s Post" <break strength="weak"/> thread on Facebook.</s> <s>"Andy\'s Post" was started on August 14, 2016 when Andy Jorgensen posted <break strength="weak"/> Testing something, <break strength="weak"/>don\'t pay any attention to this post. </s> <s>Since the original post appeared, <break strength="weak"/> hundreds of people have contributed thousands of comments, <break strength="weak"/> and those people are known as team Andy.</s> <s>They even have a theme song, <break strength="weak"/> would you like to hear it?</s></speak>'

@app.route('/')
def homepage():
    return ""

@ask.launch
def start_skill():
    global welcome_message
    print welcome_message
    return question(welcome_message)

@ask.intent("SeriouslyIntent")
def share_headlines():
    return question('<speak>Yes, <break strength="medium"/> I never joke about Andy\'s Post. Would you like to hear the theme song? </speak>')

@ask.intent("YesIntent")
def share_headlines():
    return statement('<speak>Andy\'s Post theme song. <audio src="https://s3.amazonaws.com/www.wiredforcoding.com/AndysTestPost.mp3" /></speak>')

@ask.intent("DoneIntent")
def no_intent():
    bye_text = 'Ok, sorry to bother you. I will be quiet now'
    print bye_text
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=True)