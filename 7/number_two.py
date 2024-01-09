import os
from os.path import isfile, join, isdir
import shutil

GET_PATH = '** your get dir path **'
PUT_PATH = '** your put dir path **'

class WrongPath(FileNotFoundError):
    def __init__(self, path, *args):
        super().__init__(args)
        self.path = path

    def __str__(self):
        return f"The {self.path} is not a valid path, it doesn't exist"

def file_size_finder(file_type, get_dir_path, put_dir_path):

    if not isdir(get_dir_path):
        raise WrongPath(get_dir_path)

    files = [f for f in os.listdir(get_dir_path) if isfile(join(get_dir_path, f))]
    helping_files = files[:]

    for file in helping_files:
        if not file.endswith(file_type) or file.startswith('.'):
            files.remove(file)
    
    if not isdir(put_dir_path):
        print(f"Creted directory in path: {put_dir_path}")
        os.mkdir(put_dir_path)

    for file in files:
        print(f"Copied {file} to directory in path {put_dir_path}")
        shutil.copy2(get_dir_path + '/' + file, put_dir_path)


file_size_finder('pdf', GET_PATH, PUT_PATH)