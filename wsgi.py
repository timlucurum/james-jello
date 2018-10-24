from flask import Flask
import socket

application = Flask(__name__)

@application.route("/")
def hello():
    try:
            ip = socket.gethostbyname('bbc.com')
    except:
            ip = '<no ip>'
    return "James Jello: gethostbyname = " + ip

if __name__ == "__main__":
    application.run()
