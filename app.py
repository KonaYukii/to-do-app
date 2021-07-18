from flask import Flask, request, jsonify

app = Flask(__name__)

tasklist = []

@app.route("/", methods = ['GET'])
def to_do():
  return "This application is a to do list. You can add, delete, and update things."

@app.route("/add", methods = ['POST'])
def add_task():
  req = request.json
  tasklist.append(req['content'])
  return req

@app.route("/tasklist", methods = ['GET'])
def showlist():
  return jsonify(tasklist)