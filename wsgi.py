from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "James Jello"

if __name__ == "__main__":
    application.run()
