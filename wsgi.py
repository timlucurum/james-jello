from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "G'day, From W.A."

print("G'day - 1")

if __name__ == "__main__":
    application.run()
