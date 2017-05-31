"""

Chatbot interface

Run this script to interact with the chatbot

"""


def interactWithChatbot(user_input):
    """
    Processes the user_input and come up with the correct response
    """
    # bot_brain.parse(user_input)
    return "Hello world"


if __name__ == "__main__":
    user_input = raw_input("What can I do for you? ")

    while user_input != "FINISH":
        interactWithChatbot(user_input)
        user_input = raw_input("What can I do for you? ")
