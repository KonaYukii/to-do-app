from flask import request, jsonify, Blueprint
from models import Task
# Flask is needed to build a web server using python.
# Request tells flask where we're getting our data and telling it to read it
# Jsonify provides us the form of our data

bp = Blueprint('tasklist', __name__, url_prefix = '/tasklist')

tasklist = []

@bp.route("/", methods = ['GET', 'POST'])
def task():
  if request.method == 'GET':
    return jsonify(tasklist)
  elif request.method == 'POST':
    req = request.json
    try:
      tasklist.append(req['content'])
    except: 
      return "You must use content"
    return req
# combined the get and post request together.
# request.method is just specifying what you want to do since in the beginning you wrote get and post.

@bp.route("/id/<id>", methods = ['DELETE'])
def deleteitem(id):
  id = int(id)
  try: 
    tasklist.pop(id)
  except: 
    return "No task with this " + str(id)
  return jsonify(tasklist)
# Use try and except in case users type in an id that doesnt exist
# Can only delete one at a time

@bp.route("/word/<word>", methods = ["DELETE"])
def deleteword(word):
  try:
    tasklist.remove(word)
  except:
    return word + " does not exist in list"
  return jsonify(tasklist)
# cannot delete individual words. can delete the entire task. 
# %20 for space. 
# first word is written in the url. The second is the variable that you want to delete. Makes it easier for the user to read to see whats going on.

@bp.route("/update/<id>", methods = ["PUT"])
def updateitem(id):
  id = int(id)
  try:
    req = request.json 
    tasklist[id] = req['content']
  except:
    return str(id) + " cannot be found thus cannot be updated or you must use content"
  return jsonify(tasklist)
# use put for updaate. 
# req is the new information that you're typing in.
# tasklist[id] is replacing the old information with the new req[content]