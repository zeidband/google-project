

"""get file location and return list of strings,
   each string is a line in the file"""
def read_file(file):
    file = open(file, encoding="utf8")
    sentences = file.readlines()
    file.close()
    return [sentence.strip() for sentence in sentences]


def init_data(location):
    new_data = list()
    for file in location:
        new_data += read_file(file)
    sub_strings = dict()
    for identifier, sentence in enumerate(new_data):
        length = len(sentence)
        sentence = [sentence[i:j+1] for i in range(length) for j in range(i, length)]
        for word in sentence:
            if word not in sub_strings.keys():
                sub_strings[word] = {}
                sub_strings[word]['set'] = set()
                sub_strings[word]['len'] = 0

            sub_strings[word]['set'].add(identifier)
            sub_strings[word]['len'] += 1
    return sub_strings
