import os
from os.path import isfile, join

PATH = '** your dir path **'

def file_size_finder(dir_path):
    files = [f for f in os.listdir(dir_path) if isfile(join(dir_path, f))]
    helping_files = files[:]

    sorted_dir = {}

    for file in helping_files:
        if file.startswith('.'):
            files.remove(file)
        else:
            file_stats = os.stat(PATH + '/' + file)
            name, file_type = file.split('.')
            if not file_type in sorted_dir:
                sorted_dir[file_type] = {}
            sorted_dir[file_type][name] = file_stats.st_size
    
    return sorted_dir

print(file_size_finder(PATH))