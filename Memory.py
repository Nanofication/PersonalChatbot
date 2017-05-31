"""

Blueprint of what the memories of a chatbot should consist of:

Input: *Pattern* - The text pattern of what the user says.

Output: The bot's reply

Execute: The bot may run a program. Can be empty.

Intent: What is the input's intent. What is the user's purpose with this response? Should be one purpose.

"""

class Memory:
    def __init__(self, user_input= "", output= "", functions= [], intent= ""):
        self.user_input = user_input
        self.output = output
        self.functions = functions
        self.intent = intent

        def set_intent(newIntent):
            self.intent = newIntent