from flask import Flask
from controllers import home, tasklist

app = Flask(__name__)

app.register_blueprint(home.bp)
app.register_blueprint(tasklist.bp) 