
"""
get file location and return list of strings,
each string is a line in the file
"""
def read_file_as_list(file):
    with open(file, encoding="utf8") as f:
        sentences = f.readlines()
    f.close()
    return [sentence.strip() for sentence in sentences]


"""
get list of name files 
return a list with all the sentences from the file
and a dictionary with all the substring of the list sentences as keys 
"""
def init_data(location):
    # read all files
    new_data = list()
    for file in location:
        new_data += read_file_as_list(file)

    # go over every string and add to the dictionary all its substring as keys
    sub_strings = dict()
    for identifier, sentence in enumerate(new_data):
        length = len(sentence)
        sentence = [sentence[i: j + 1] for i in range(length) for j in range(i, length)]
        for word in sentence:
            sub_strings.update({word: {identifier}}) if word not in sub_strings.keys() else sub_strings[word].add \
                (identifier)

    return new_data, sub_strings
