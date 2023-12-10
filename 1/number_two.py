lista = ['Ala', 'ma', 'kota', 'oraz', 'raDar', 'Kajak', 'Kamil Ślimak']

def funk(list_of_words):
    result = []
    for i in list_of_words:
        word = i.lower()[::-1]
        if i.lower() != word:
            result.append(word)
    return result


print(funk(lista))