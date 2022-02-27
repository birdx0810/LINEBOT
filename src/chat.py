import nltk

import re
import random

PAIRS = nltk.chat.eliza.pairs
REFLECTIONS = nltk.chat.util.reflections

class ElizaBot(nltk.chat.util.Chat):
    """
    Inherit from `nltk.chat.eliza.eliza_chatbot` module and modify converse function
    """
    def __init__(
        self, 
        pairs=PAIRS, 
        reflections=REFLECTIONS,
    ):
        super().__init__(pairs=pairs, reflections=reflections)
        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def converse(
        self, 
        user_input, 
        quit=["goodbye", "good bye", "bye", "see you"]
    ):
        """Override the original converse model of the nltk.util.Chat class
        """
        # If user ends conversation, return one of escapes
        if user_input.lower() in self._escapes:
            return random.choice(self._escapes)
        # Chat with ELIZA otherwise
        while user_input[-1] in "!.":
            user_input = user_input[:-1]
        response = self.respond(user_input)

        return response

if __name__=="__main__":
    bot = ElizaBot()
    while True:
        i = input("> ")
        resp = bot.converse(i)
        print(resp)


