from . import app, api

from ros_models import *


from flask_restful import Resource

@app.route('/')
def index():
    return 'DotBot Main Page!'



class RosMaster(Resource):
    def __init__(self):
        self.master = Master()
    def post(self):
        self.master.run()
        return {'response': 'ok'}

    def delete(self):
        self.master.kill()
        return {'response': 'ok'}


api.add_resource(RosMaster, '/roscore')
