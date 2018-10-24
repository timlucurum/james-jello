from flask import Flask
import socket

application = Flask(__name__)

@application.route("/")
def hello():
    try:
            ip = socket.gethostbyname('crisis-melba')
    except:
            ip = '<no ip>'
    return "James Jello: gethostbyname = " + ip

if __name__ == "__main__":
    application.run()
