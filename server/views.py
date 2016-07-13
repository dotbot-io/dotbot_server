from . import app, api

from ros_models import *


from flask_restful import Resource

@app.route('/')
def index():
    return 'DotBot Main Page!'


master = Master()
node = Node('turtlesim', 'turtlesim_node')

class RosMaster(Resource):
    def post(self):
        master.run()
        return {'response': 'ok'}

    def delete(self):
        master.kill()
        return {'response': 'ok'}


class RosNode(Resource):
    def post(self):
        node.run()
        return {'response': 'ok'}

    def delete(self):
        node.kill()
        return {'response': 'ok'}



api.add_resource(RosMaster, '/roscore')
api.add_resource(RosNode, '/turtlesim')
