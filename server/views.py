from . import app

from ros_models import *

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/roscore')
def runmaster():
    m = Master()
    m.run()
    return 'ok'

@app.route('/turtlesim')
def turtlesim():
    m = Node('turtlesim', 'turtlesim_node')
    m.run()
    return 'ok'
