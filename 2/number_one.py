import json

FILE_PATH = "** put your path **"

OUT_FILE_PATH = '** put your path **'



def count_words(read_path, write_path, l):

    ls = []
    words = []

    with open(read_path, 'r') as file:
        for line in file:
            ls.append(line.strip())

    if l < len(ls):
        lines = ls[:l]
    else:
        lines = ls[:]

    print(lines)

    for i in lines:
        x = i.split(' ')
        for j in x:
            if not '' == j:
                words.append(j.strip())

    words_counted = {}
    helping_words = words[:]

    for i in range(len(words)):
        x = 0
        while words[i] in helping_words:
            y = helping_words.index(words[i])
            x += 1
            helping_words.pop(y)
            words_counted[words[i]] = x

    with open(write_path, 'w') as outfile:
        json.dump(words_counted, outfile, indent=2)

#count_words(FILE_PATH, OUT_FILE_PATH, 3)
count_words(FILE_PATH, OUT_FILE_PATH, 8)