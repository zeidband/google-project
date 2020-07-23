import re
import string

class Data:

    def __init__(self, location):
        self.sentences = list()
        self.sub_sentences = dict()
        self.init_data(location)
        self.data = list()

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
        num = 0
        for file in location:
            self.sentences += self.read_file_as_list(file)
            if num == 300:
                break
            num += 1

        # go over every string and add to the dictionary all its substring as keys
        self.sub_sentences = dict()
        for identifier, sentence in enumerate(self.sentences):
            curr_sentence = ' '.join((''.join(i for i in sentence if i in string.ascii_letters + ' ')).split())
            length = len(curr_sentence)
            curr_sentence = [curr_sentence[i: j + 1] for i in range(length) for j in range(i, length)]
            if len(curr_sentence) != 0:
                for word in curr_sentence:
                    curr_word = word.strip()
                    self.sub_sentences.update({curr_word: {identifier}}) \
                        if curr_word not in self.sub_sentences.keys() \
                        else self.sub_sentences[curr_word].add(identifier)

        return self
