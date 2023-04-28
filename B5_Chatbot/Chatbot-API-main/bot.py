import warnings
import transformers
import os
import datetime
import numpy as np

"""
This module defines the ChatBot class that can interact with users through a conversational pipeline using the DialoGPT-medium model from Microsoft.

Functions:
- init(self, channel): Initializes the ChatBot object with a specific channel name and loads the DialoGPT-medium model for conversational pipeline.
- warnings_off(self): Disables the future warning that warns about modifying the pretrained model configuration to control generation.
- wake_up(self, text): Determines if the ChatBot is mentioned in the user's message and returns True if it is.
- action_time(self): Returns the current time as a string in the format of "HH:MM".
- polite_response(self): Returns a random polite response string from a set of pre-defined strings.
- goodbye_response(self): Returns a random goodbye response string from a set of pre-defined strings.
- getResponse(self, query): Receives a user message as input, determines its intent, and returns an appropriate response string.

Attributes:
- channel: The name of the channel assigned to the ChatBot object.
- nlp: The DialoGPT-medium model used for generating conversational responses.
- text: The most recent user message processed by the ChatBot.

Usage:
- To create a ChatBot object, call the constructor and provide a channel name: bot = ChatBot("my_channel")
- To get a response from the ChatBot, call the getResponse method and provide a user message as input: response = bot.getResponse("Hello")
"""


class ChatBot:
    def __init__(self, channel):
        print(f"-----Starting Model : {channel}-----")
        self.channel = channel
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        self.nlp = transformers.pipeline(
            "conversational", model="microsoft/DialoGPT-medium")
        os.environ["TOKENIZERS_PARALLELISM"] = "true"
        self.warnings_off()

    def warnings_off(self):
        warnings.filterwarnings(
            "ignore", message="You have modified the pretrained model configuration to control generation. This is a deprecated strategy to control generation and will be removed soon, in a future version.")

    def wake_up(self, text):
        return True if self.channel.lower() in text.lower() else False

    def action_time(self):
        return datetime.datetime.now().time().strftime("%H:%M")

    def polite_response(self):
        return np.random.choice(
            [
                "You're welcome!",
                "Anytime!",
                "No problem!",
                "Cool!",
                "I'm here if you need me!",
                "Mention not",
            ]
        )

    def goodbye_response(self):
        return np.random.choice(
            [
                "Tata",
                "Have a good day",
                "Bye",
                "Goodbye",
                "Hope to meet soon",
                "Peace out!",
            ]
        )

    def getResponse(self, query):
        self.text = query

        if self.wake_up(self.text) is True:
            res = "Hello I am AlTron the AI, what can I do for you?"
        elif "who made you" in self.text.lower():
            res="I was made by Gladingi_BOi" 
        elif "time" in self.text:
            res = self.action_time()
        elif any(i in self.text for i in ["thank", "thanks"]):
            res = self.polite_response()
        elif any(i in self.text for i in ["exit", "close", "bye"]):
            res = self.goodbye_response()
        else:
            if self.text == "ERROR":
                res = "Sorry, come again?"
            else:
                chat = self.nlp(transformers.Conversation(
                    self.text), pad_token_id=50256, max_length=100)
                res = str(chat)
                res = res[res.find("bot >> ") + 6:].strip()
        return res
