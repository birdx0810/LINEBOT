# from nltk.chat import eliza, util
import nltk

import re
import random

pairs = nltk.chat.eliza.pairs
reflections = nltk.chat.util.reflections

class elizaBot(nltk.chat.util.Chat):
    '''
    Inherit from `nltk.chat.eliza.eliza_chatbot` module and modify converse function
    '''
    def __init__(self, pairs, reflections={}):
        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()
        # Add list of words that mark EOC
        self.escape = ["bye", "good bye", "goodbye"]

    def converse(self, user_input):
        """Overrides the original converse model of the nltk.util.Chat class
        """
        if user_input.lower() in self.escape:
            return user_input
        while user_input[-1] in "!.":
            user_input = user_input[:-1]
        response = self.respond(user_input)
        return response

if __name__=="__main__":
    bot = elizaBot(pairs, reflections)
    while True:
        i = input("> ")
        resp = bot.converse(i)
        print(resp)

