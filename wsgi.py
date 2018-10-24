from flask import Flask
import requests

application = Flask(__name__)

@application.route("/")
def hello():
    try:
            data = requests.get('http://crisis-melba:8080')
    except:
            data = '<no data>'
    return "James Jello: data = " + data

if __name__ == "__main__":
    application.run()
