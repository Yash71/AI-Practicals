from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import bot

"""
This module defines a Flask application that provides a RESTful API for interacting with a ChatBot object.

Functions:
- post(self): Processes a POST request sent to the '/bot' endpoint, extracts a user message from the request body, sends the message to the ChatBot object to generate a response, and returns the response as a JSON object.

Attributes:
- app: The Flask application object that provides the RESTful API.
- api: The Flask-Restful API object that handles the routing of requests.
- chatbot: The ChatBot object that is used to generate responses to user messages.

Usage:
- To run the Flask application, call the 'run' method on the app object from the command line: 'python app.py'
- To interact with the ChatBot, send a POST request to the '/bot' endpoint of the running Flask application, passing a JSON object in the following format: {'message': 'Hello'}. The ChatBot will generate a response based on the message and return it as a JSON object in the following format: {'message': 'Hi there!'}.
"""


app = Flask(__name__)
api = Api(app)
CORS(app)

chatbot = bot.ChatBot(channel="AlTron")

class Bot(Resource):
    def get(self):
        message = request.args.get('message')
        message = message.replace("%20"," ")
        reply = chatbot.getResponse(query=message)
        response = {'message': str(reply)}
        return response

api.add_resource(Bot, '/bot')

if __name__ == '__main__':
    app.run(debug=True, port=5002, use_reloader = False)
