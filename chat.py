from nltk.chat import eliza, util

import nltk

import re
import random

pairs = eliza.pairs
reflections = util.reflections

class elizaBot(util.Chat):
    '''
    Inherit from `nltk.chat.eliza.eliza_chatbot` module and modify converse function
    '''
    def __init__(self, pairs, reflections={}):
        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()
        # Add list of words that mark EOC
        self.escape = ["Bye", "Good Bye", "good bye"]

    # Override `converse` function
    def converse(self, user_input=None):
        quit = self.escape
        if user_input == None:
            user_input = ""
        
        # If input is not in quit
        while user_input not in quit:
            user_input = quit

            # Get user input
            try:
                user_input = input(">")
            except EOFError:
                print(user_input)
            
            # Return reply
            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                print(self.respond(user_input))

if __name__=="__main__":
    bot = elizaBot(pairs, reflections)
    bot.converse()

