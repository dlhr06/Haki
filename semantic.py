import os

def file_exists(filename)-> bool:
        return os.path.isfile(filename)