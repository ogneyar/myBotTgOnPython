import flask
app = flask.Flask(__name__)

@app.route("/")
def site():
    #do whatevr here...
    return "Hello Heroku"