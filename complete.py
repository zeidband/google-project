import string

def delete_character(input_, sentences):
    for i in range(len(input_)):
        if input_[:i] + input_[i + 1:] in sentences.keys():
            print("FOR DEBUG: delete sentence")
            return sentences[input_[:i] + input_[i + 1:]], i

    return None, -1


def replace_character(sentence, sentences):
    result = set()
    for letter in string.ascii_letters:
        for character in range(len(sentence)):
            change_sentence = sentence[:character] + letter + sentence[character + 1:]
            if change_sentence in sentences.keys():
                result = result.union(sentences[change_sentence])
                if len(result) >= 5:
                    return list(result)[:5]
    return result


def get_best_k_completions(sentence, data, sentences):
    # check if the sentence is complete in the data
    if sentence in sentences.keys():
        return sentences[sentence]

    # else try to delete character
    set_id_sentences, key = delete_character(sentence, sentences)
    if set_id_sentences is not None:
        return set_id_sentences
    # TODO: check if the answer len = 5

    set_id_sentences = replace_character(sentence, sentences)
    if len(set_id_sentences) != 0:
        return set_id_sentences

    # set_id_sentences = add_character(sentence, sentences)
    return None


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

