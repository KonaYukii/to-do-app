from flask import Flask, request, jsonify
# Flask is needed to build a web server using python.
# Request tells flask where we're getting our data and telling it to read it
# Jsonify provides us the form of our data

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

@app.route("/deletetask/<id>", methods = ['DELETE'])
def deleteitem(id):
  id = int(id)
  try: 
    tasklist.pop(id)
  except: 
    return "No task with this " + str(id)
  return jsonify(tasklist)
# Use try and except in case users type in an id that doesnt exist
# Can only delete one at a time

@app.route("/deleteword/<word>", methods = ["DELETE"])
def deleteword(word):
  try:
    tasklist.remove(word)
  except:
    return word + " does not exist in list"
  return jsonify(tasklist)
# cannot delete individual words. can delete the entire task. 
# %20 for space. 