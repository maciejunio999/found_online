import json

READ_FILE_PATH = "** your path **"
WRITE_FILE_PATH = "** your path **"


def count_letters(read_path, write_path):
    string = ''
    with open(read_path, 'r') as file:
        for line in file:
            l = line.lower().replace(' ', '').replace('\n', '')
            string += l

    letters = {}
    numer_of_letters = len(string)

    for i in string:
        if i in letters.keys():
            letters[i]['count'] += 1
        else:
            letters[i] = {'count': 1, 'freq': 0}
    
    for i in letters:
        letters[i]['freq'] = round(letters[i]['count']/numer_of_letters, 2)
    
    with open(write_path, 'w') as outfile:
        json.dump(letters, outfile, indent=3)

count_letters(READ_FILE_PATH, WRITE_FILE_PATH)
