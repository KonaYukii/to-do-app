from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def to_do():
  return "This application is a to do list. You can add, delete, and update things."