from flask import request, jsonify, Blueprint
from models.Task import Task
from app import db
# Flask is needed to build a web server using python.
# Request tells flask where we're getting our data and telling it to read it
# Jsonify provides us the form of our data

bp = Blueprint('tasklist', __name__, url_prefix = '/tasklist')

@bp.route("/", methods = ['GET', 'POST'])
def task():
  if request.method == 'GET':
    tasks = Task.query.all()
    # SELECT * from Task
    tasklist = [] 
    # To show the user the tasklist they created
    for task in tasks:
      # running through each task in the variable tasks
      tasklist.append(task.content)
      # adding each task content to the tasklist
    return jsonify(tasklist)
  elif request.method == 'POST':
    req = request.json
    # gets what you wrote in the body and stores it in the variable req
    try:
      task = Task(content = req['content'])
      # gets the content of the req and puts it in the content argument which belongs to the Task Model.
      db.session.add(task)
      # preparing the task to the database
      db.session.commit()
      # add the req[content] to the database
    except: 
      return "You must use content"
    return req
# combined the get and post request together.
# request.method is just specifying what you want to do since in the beginning you wrote get and post.

@bp.route("/id/<id>", methods = ['DELETE'])
def deleteitem(id):
  id = int(id)
  try: 
    task = Task.query.get(id)
    # SELECT * FROM Task WHERE id = <id>
    db.session.delete(task)
    db.session.commit()
  except: 
    return "No task with this " + str(id)
  tasks = Task.query.all()
  tasklist = [] 
  for task in tasks:
    tasklist.append(task.content)
  return jsonify(tasklist)
# Use try and except in case users type in an id that doesnt exist
# Can only delete one at a time

@bp.route("/word/<word>", methods = ["DELETE"])
def deleteword(word):
  try:
    tasks = Task.query.filter_by(content = word).all()
    # SELECT * FROM Task WHERE content = <word>
    for task in tasks:
      db.session.delete(task)
    db.session.commit()
  except:
    return word + " does not exist in list"
  tasks = Task.query.all()
  tasklist = [] 
  for task in tasks:
    tasklist.append(task.content)
  return jsonify(tasklist)
# cannot delete individual words. can delete the entire task. 
# %20 for space. 
# first word is written in the url. The second is the variable that you want to delete. Makes it easier for the user to read to see whats going on.

@bp.route("/update/<id>", methods = ["PUT"])
def updateitem(id):
  id = int(id)
  try:
    req = request.json 
    task = Task.query.get(id)
    # SELECT * FROM Task WHERE id = <id>
    task.content = req['content']
    # Replace current task content with req[content]
    db.session.add(task)
    db.session.commit()
  except:
    return str(id) + " cannot be found thus cannot be updated or you must use content"
  tasks = Task.query.all()
  tasklist = [] 
  for task in tasks:
    tasklist.append(task.content)
  return jsonify(tasklist)
# use put for updaate. 
# req is the new information that you're typing in.
# tasklist[id] is replacing the old information with the new req[content]