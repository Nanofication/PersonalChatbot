"""

A representation of JSON files and its list of memories

"""

class MemoryFile():
    def __init__(self, file_name, memories = []):
        self.file_name = file_name
        self.memories = memories