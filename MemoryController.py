"""

Controls how information is added, processed or deleted in specific JSON files


"""
import json
import os

from MemoryFile import MemoryFile
from Memory import Memory

from Tkinter import *

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

def displayMemories():
    """
    Display JSON files and its contents with associated fields
    Note: This will have to be in a GUI later
    """
    loadMemories()

    for m in MEMORY_LIST:
        print "File Name: ", m.file_name
        for i in range(len(m.memories)):
            print "Memory Number: ", i
            print "User Input: ", m.memories[i].user_input
            print "Intent: ", m.memories[i].intent
            print "Functions: ", m.memories[i].functions
            print "Output: ", m.memories[i].output
            print "\n"

def displayMemoriesInGUI():
    """
    Display JSON files and its contents with associated fields inside the GUI
    :return:
    """
    for m in MEMORY_LIST:
        print "File Name: ", m.file_name
        for i in range(len(m.memories)):
            print "Memory Number: ", i
            print "User Input: ", m.memories[i].user_input
            print "Intent: ", m.memories[i].intent
            print "Functions: ", m.memories[i].functions
            print "Output: ", m.memories[i].output
            print "\n"

def createNewMemory():
    """
    Create a new memory with user input
    :return: Memory object
    """
    print "Add a New Memory\n"
    user_input = raw_input("Provide a user input: ")
    intent = raw_input("What is the intent of the input: ")
    functions = raw_input("What functions will the chatbot execute: ")
    output = raw_input("What will the chatbot respond with: ")

    return Memory(user_input, intent, functions, output)


def addToMemories(memory, memoryFile):
    """
    Add memory to the list of memories
    :param memory: Memory object that will be stored
    """
    global MEMORY_LIST
    new_memory = createNewMemory()

    memoryFile.memories.append(new_memory)


if __name__ == "__main__":
    loadMemories()

    # Create GUI Window
    root = Tk()

    # Modify Root Window
    root.title("Memory Controller")
    root.geometry("720x576")

    app = Frame(root)
    app.grid()

    for memory_file in MEMORY_LIST:
        label = Label(app, text = memory_file.file_name)
        label.grid()

    # Kick off event loop
    root.mainloop()