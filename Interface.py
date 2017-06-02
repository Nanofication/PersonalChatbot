"""

Chatbot interface

Run this script to interact with the chatbot

"""

import Brain


def interactWithChatbot(user_input):
    """
    Processes the user_input and come up with the correct response
    """
    memory = Brain.parseUserInput(user_input)
    if memory != None:
        print Brain.processMemory(memory)
    else:
        print "I did not catch that"


if __name__ == "__main__":
    Brain.parseMemoryDB()
    print "What can I do for you?"
    user_input = raw_input(">: ")

    while user_input != "FINISH":
        interactWithChatbot(user_input)
        print "What else can I do for you?"
        user_input = raw_input(">: ")
