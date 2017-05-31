"""

Brain of Personal Chatbot

All memory that needs to be loaded, functions that needs to be executed and
questions to be parsed will be done here.

"""

import json
import os
import re

from Memory import Memory

PATH_TO_JSON = 'MemoryDB/'
FILE_DIR = os.listdir(PATH_TO_JSON)
MEMORIES = dict()

"""
Load Memories
"""

def parseMemoryDB():
    """
    Read all the chatbot's memories from the file and store them into a dictionary of user_inputs
    mapped to memory objects

    """
    global MEMORIES
    json_files = getListOfJsonFiles()


    for index, js in enumerate(json_files):
        with open(os.path.join(PATH_TO_JSON, js)) as json_file:
            json_text = json.load(json_file)

            for data in json_text['memories']:
                memory = Memory(removeSpecialChars(data['input']), data['output'], data['functions'], data['intent'])
                MEMORIES[memory.user_input] = memory


def getListOfJsonFiles():
    """
    Get list of json files from the director
    :return: List of json files
    """
    json_files = [json_file for json_file in FILE_DIR if json_file.endswith('.json')]
    return json_files


"""
Parse User Input
"""

def parseUserInput(user_input):
    """
    Parse the user_input and return the memory associated with it
    :return: Memory object associated with the user_input
    Throw statement if no memory was found
    """
    global MEMORIES
    user_input = removeSpecialChars(user_input)
    try:
        return MEMORIES[user_input]
    except:
        print "Memory not found"
        return None

def removeSpecialChars(content):
    """
    Strip the content of special characters
    :return: The lower cased content stripped of special characters
    """
    pattern = re.compile("[^0-9a-zA-Z]+")
    content = pattern.sub(' ', content.lower())
    return content

def processMemory(memory):
    """
    Extract the contents of the memory, run the functions required and return the correct output
    :param memory: Memory object
    :return: The memory's output
    """

    return memory.output

if __name__ == "__main__":
    parseMemoryDB()
    memory = parseUserInput("Hi")
    processMemory(memory)