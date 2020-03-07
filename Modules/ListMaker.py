import os
import re

class ListMaker:

    def __init__(self, input_path):
        self.input_path = input_path

    def list_files(self):
        self.file_list = os.listdir(self.input_path)
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(self.file_list) for self.file_list in re.split('([0-9]+)', key)]
        return sorted(self.file_list, key=alphanum_key)