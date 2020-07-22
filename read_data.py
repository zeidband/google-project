
class Data:

    def __init__(self, location):
        self.sentences = list()
        self.sub_sentences = dict()
        self.init_data(location)

    """
    get file location and return list of strings,
    each string is a line in the file
    """
    def read_file_as_list(self, file):
        with open(file, encoding="utf8") as f:
            sentences = f.readlines()
        f.close()
        return [sentence.strip() for sentence in sentences]

    """
    get list of name files 
    return a list with all the sentences from the file
    and a dictionary with all the substring of the list sentences as keys 
    """
    def init_data(self, location):
        # read all files
        self.sentences = list()
        for file in location:
            self.sentences += self.read_file_as_list(file)

        # go over every string and add to the dictionary all its substring as keys
        self.sub_sentences = dict()
        for identifier, sentence in enumerate(self.sentences):
            length = len(sentence)
            sentence = [sentence[i: j + 1] for i in range(length) for j in range(i, length)]
            for word in sentence:
                self.sub_sentences.update({word: {identifier}}) \
                    if word not in self.sub_sentences.keys() \
                    else self.sub_sentences[word].add(identifier)

        return self
