import string
from auto_complete_data import AutoCompleteData


class Complete:

    def __init__(self, data, len_result=5):
        self.data = data
        self.LEN_RESULT = len_result
        self.__complete_sentences = []

    def get_reduce_points(self, i):
        return - 10 + 2 * (i - 1) if i < 4 else -2

    def is_exist(self, sentence):
        for s in self.__complete_sentences:
            if s.get_complete_sentences() == sentence:
                return True
        return False

    def add_complete_sentence(self, sentence, score):
        if sentence in self.data.sub_sentences.keys():

            for id_ in self.data.sub_sentences[sentence]:

                if not self.is_exist(self.data.sentences[id_]):
                    self.__complete_sentences.append(AutoCompleteData(self.data.sentences[id_], score))

                    if len(self.__complete_sentences) == self.LEN_RESULT:
                        return True

        return False

    def change_input(self, input_):
        len_ = len(input_)

        for i in range(len_ - 1, -1, -1):

            score = self.get_reduce_points(i)

            for letter in string.ascii_letters:

                if self.add_complete_sentence(input_[:i] + letter + input_[i + 1:], 2 * (len_ - 1) + score // 2):
                    return

                if self.add_complete_sentence(input_[:i] + letter + input_[i:], 2 * (len_ - 1) + score):
                    return

            if self.add_complete_sentence(input_[:i] + input_[i + 1:], 2 * (len_ - 1) + score // 2):
                return

    def get_best_k_completions(self, input_):
        self.__complete_sentences.clear()
        # check if the sentence is complete in the data
        if self.add_complete_sentence(input_, 2 * len(input_)):
            return self.__complete_sentences

        # else try to change the input
        self.change_input(input_)
        return self.__complete_sentences

    # class Complete:
#     def __init__(self, init_data, text):
#         self.initData = init_data
#         self.txt_input = text
#         self.suitable_sentence = []
#         print(self.find_best_complete())

#     def get_complete_by_word(self, key):
#         return [self.initData.sentence_data[k] for k in self.initData.substringData[key]]

#     def find_best_complete(self):
#         while len(self.suitable_sentence) < 5:
#             if self.txt_input in self.initData.substringData:
#                 self.suitable_sentence += [self.initData.sentence_data[k] for k in self.initData.substringData[self.txt_input]]
#             else:
#                 self.delete_char()

