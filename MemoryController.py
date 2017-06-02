"""

Controls how information is added, processed or deleted in specific JSON files


"""
import json
import os

from MemoryFile import MemoryFile
from Memory import Memory

PATH_TO_JSON = 'MemoryDB/'
FILE_DIR = os.listdir(PATH_TO_JSON)
MEMORY_LIST = []

def loadMemories():
    """
    Read chatbot's individual memory files and stores them into a list of memory files
    """
    global MEMORIES
    json_files = getListOfJsonFiles()

    for index, js in enumerate(json_files):
        memoryFile = MemoryFile(js)

        with open(os.path.join(PATH_TO_JSON, js)) as json_file:
            json_text = json.load(json_file)
            for data in json_text['memories']:
                memory = Memory(data['input'], data['output'], data['functions'], data['intent'])
                memoryFile.memories.append(memory)
        MEMORY_LIST.append(memoryFile)

def getListOfJsonFiles():
    """
    Get list of json files from the director
    :return: List of json files
    """
    json_files = [json_file for json_file in FILE_DIR if json_file.endswith('.json')]
    return json_files

loadMemories()

for m in MEMORY_LIST:
    print m.file_name
    for memory in m.memories:
        print memory.user_input
        print memory.output