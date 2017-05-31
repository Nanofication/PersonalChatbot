"""

Brain of Personal Chatbot

All memory that needs to be loaded, functions that needs to be executed and
questions to be parsed will be done here.

"""

import json
import os

from Memory import Memory
from pprint import pprint

PATH_TO_JSON = 'MemoryDB/'
FILE_DIR = os.listdir(PATH_TO_JSON)

def parseMemoryDB():
    """
    Read all the chatbot's memories from the file and store them into a dictionary of user_inputs
    mapped to memory objects

    :return: Dictionary of user inputs mapped to memory objects
    """
    memory = Memory()

def getListOfJsonFiles():
    """
    Get list of json files from the director
    :return: List of json files
    """
    json_files = [json_file for json_file in FILE_DIR if json_file.endswith('.json')]
    return json_files

print getListOfJsonFiles()
# def parse_memories():