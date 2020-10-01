# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'STMicroelectronics'}

class Hello_user(Resource):
    def get(self, username):
        # Set the response code to 201
         return 'Why Hello %s!\n' % username

api.add_resource(HelloWorld, '/','/hello/')
api.add_resource(Hello_user, '/hello/<username>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='30000')