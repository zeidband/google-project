
from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    """source_text, offset,"""
    def __init__(self, sentence, score):
        self.__completed_sentence = sentence
        # self.__source_text = source_text
        # self.__offset = offset
        self.__score = score

    def addScore(self, num):
        self.__score += num

    def get_complete_sentences(self):
        return self.__completed_sentence

    def get_score(self):
        return self.__score
