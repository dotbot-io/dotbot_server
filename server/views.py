from . import app, api

from ros_models import *


from flask_restful import Resource, reqparse

@app.route('/')
def index():
    return 'DotBot Main Page!'


master = Master()
node = Node('turtlesim', 'turtlesim_node')
launch = Launch('rosbridge_server', 'rosbridge_websocket.launch')

class RosMaster(Resource):
    def post(self):
        master.run()
        return {'response': 'ok'}

    def delete(self):
        master.kill()
        return {'response': 'ok'}


class RosNode(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('package')
        parser.add_argument('name')
        args = parser.parse_args()
        
        return {'response': 'ok'}

    def delete(self):
        return {'response': 'ok'}



class RosLaunch(Resource):
    def post(self):
        launch.run()
        return {'response': 'ok'}

    def delete(self):
        launch.kill()
        return {'response': 'ok'}

class TurtleTeleopNode(Resource):
    def post(self):
        node.run()
        return {'response': 'ok'}

    def delete(self):
        node.kill()
        return {'response': 'ok'}


class TurtleNode(Resource):
    def post(self):
        node.run()
        return {'response': 'ok'}

    def delete(self):
        node.kill()
        return {'response': 'ok'}




api.add_resource(RosMaster, '/roscore')
api.add_resource(RosNode, '/rosnode')
api.add_resource(RosLaunch, '/rosbridge')
api.add_resource(TurtleNode, '/turtlesim')
api.add_resource(TurtleTeleopNode, '/teleop')
