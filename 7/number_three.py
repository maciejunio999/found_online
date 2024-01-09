import os
from os.path import isfile, join, isdir

PATH = '** your dir path **'

def sum_of_lists(list1, list2):
    suma = list2[:]
    for i in list1:
        if i not in list2:
            suma.append(i)
    return suma

def file_size_finder(dict_path):
    files = [f for f in os.listdir(dict_path) if isfile(join(dict_path, f))]
    dirs = [f for f in os.listdir(dict_path) if isdir(join(dict_path, f))]
    helping_files = files[:]

    print(files)
    print(dirs)

    for file in helping_files:
        if file.startswith('.'):
            files.remove(file)
    
    for dir in dirs:
        new_files = [(dir + '/' + f) for f in os.listdir(dict_path + '/' + dir) if isfile(join(dict_path + '/' + dir, f))]
        new_dirs = [(dir + '/'  + f) for f in os.listdir(dict_path + '/' + dir) if isdir(join(dict_path + '/' + dir, f))]
        for new_file in new_files:
            files.append(new_file)
        for new_dir in new_dirs:
            dirs.append(new_dir)
        
    print(files)
    print(dirs)
    #return sorted_dir

file_size_finder(PATH)