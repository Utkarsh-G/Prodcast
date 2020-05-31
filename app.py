# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
	def get(self):
		with open('world.json') as json_file:
			world_dictionary = json.load(json_file)
		return world_dictionary


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
