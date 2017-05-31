"""

Brain of Personal Chatbot

All memory that needs to be loaded, functions that needs to be executed and
questions to be parsed will be done here.

"""

import json
import os

from Memory import Memory

PATH_TO_JSON = 'MemoryDB/'
FILE_DIR = os.listdir(PATH_TO_JSON)

def parseMemoryDB():
    """
    Read all the chatbot's memories from the file and store them into a dictionary of user_inputs
    mapped to memory objects

    :return: Dictionary of user inputs mapped to memory objects
    """
    json_files = getListOfJsonFiles()
    memories = dict()

    for index, js in enumerate(json_files):
        with open(os.path.join(PATH_TO_JSON, js)) as json_file:
            json_text = json.load(json_file)

            for data in json_text['memories']:
                memory = Memory(data['input'], data['output'], data['functions'], data['intent'])
                memories[memory.user_input] = memory
    return memories

def getListOfJsonFiles():
    """
    Get list of json files from the director
    :return: List of json files
    """
    json_files = [json_file for json_file in FILE_DIR if json_file.endswith('.json')]
    return json_files



# def parse_memories():