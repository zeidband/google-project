import string

# TODO: complete


class Complete:

    def __init__(self, data, len_result=5):
        self.data = data
        self.suitable_sentences = set()
        self.LEN_RESULT = len_result
        self.__count_sentences = 0
        self.suitable_complete_sentence = set()

    def delete_character(self, input_):
        for i in range(len(input_)):
            if input_[:i] + input_[i + 1:] in self.data.sub_sentences.keys():
                self.suitable_complete_sentence = self.suitable_complete_sentence.union(input_[:i] + input_[i + 1:])

    def replace_character(self, input_, flag):
        for letter in string.ascii_letters:
            for index in range(len(input_)):
                change_sentence = input_[:index] + letter + input_[index + 1:]

                if change_sentence in self.data.sub_sentences.keys():
                    self.suitable_complete_sentence = self.suitable_complete_sentence.union(self.data.sub_sentences[change_sentence])

    def add_character(self, input_):
        for letter in string.ascii_letters:
            for character in range(len(input_)):
                change_sentence = input_[:character] + letter + input_[character:]

                if change_sentence in self.data.sub_sentences.keys():
                    self.suitable_complete_sentence = self.suitable_complete_sentence.union(self.data.sub_sentences[change_sentence])

    def get_best_k_completions(self, input_):
        # check if the sentence is complete in the data
        if input_ in self.data.sub_sentences.keys():
            self.suitable_sentences = self.data.sub_sentences[input_]

        # else try to change the input
        self.__count_sentences = len(self.suitable_sentences)
        if self.__count_sentences < self.LEN_RESULT:
            self.delete_character(input_)
            self.replace_character(input_)
            self.add_character(input_)


# class Complete:
#     def __init__(self, init_data, text):
#         self.initData = init_data
#         self.txt_input = text
#         self.suitable_sentence = []
#         print(self.find_best_complete())
#     def get_complete_by_word(self, key):
#         return [self.initData.sentence_data[k] for k in self.initData.substringData[key]]
#     def delete_char(self):
#         for char in self.txt_input:
#             if self.txt_input.replace(char, "") in self.initData.substringData:
#                 self.suitable_sentence += self.get_complete_by_word(self.txt_input.replace(char, ""))
#     def replace_char(self):
#
#     def add_char(self):
#         pass
#     def find_best_complete(self):
#         while len(self.suitable_sentence) < 5:
#             if self.txt_input in self.initData.substringData:
#                 self.suitable_sentence += [self.initData.sentence_data[k] for k in self.initData.substringData[self.txt_input]]
#             else:
#                 self.delete_char()

